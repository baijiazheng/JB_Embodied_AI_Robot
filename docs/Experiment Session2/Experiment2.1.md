Experiment:HC_SR04 test

Goal:test the link and achieve the sensor's function.

Hardware:Robot, Computer

Communication: Nomachine

Input:run the python example project

Output:every 2 seconds print how far between it and obstacle

What I learned:How can S100 use sensor. -use python with port 


```
#!/usr/bin/env python3
import sys
import signal
import os
import Hobot.GPIO as GPIO
import time

# ===================== 核心配置（已改为19/21引脚）=====================
TRIG_PIN = 19   # 触发引脚改为BOARD 19
ECHO_PIN = 21   # 回声引脚改为BOARD 21
SOUND_SPEED = 34300  # 声速(cm/s)，可按温度微调
TIMEOUT = 0.2         # 超时阈值（放宽到0.2秒）
MEASURE_INTERVAL = 1.0# 测距间隔（避免频繁触发）

# ===================== 新增：强制释放GPIO引脚 =====================
def release_gpio(pin):
    """手动释放指定BOARD编号的GPIO引脚，解决资源占用问题"""
    try:
        # 转换BOARD编号到系统GPIO编号（适配地平线板卡映射规则）
        gpio_num = pin
        if hasattr(GPIO, 'BOARD_TO_BCM') and pin in GPIO.BOARD_TO_BCM:
            gpio_num = GPIO.BOARD_TO_BCM[pin]
        
        # 强制取消导出
        unexport_path = "/sys/class/gpio/unexport"
        if os.path.exists(unexport_path):
            with open(unexport_path, 'w') as f:
                f.write(str(gpio_num))
        time.sleep(0.1)
    except Exception as e:
        print(f"⚠️  释放引脚{pin}警告：{e}（非关键错误，继续运行）")

# ===================== 信号处理（优雅退出）=====================
def signal_handler(signal_num, frame):
    """捕获Ctrl+C，清理GPIO并退出"""
    print("\n🛑 接收到退出信号，清理GPIO资源...")
    GPIO.cleanup()
    release_gpio(TRIG_PIN)
    release_gpio(ECHO_PIN)
    sys.exit(0)

# ===================== 测距核心函数 =====================
def measure_distance():
    """单次测距，返回距离值(cm)，失败返回None"""
    # 1. 复位TRIG电平（避免电平卡死）
    GPIO.output(TRIG_PIN, GPIO.LOW)
    time.sleep(0.001)

    # 2. 发送10us高电平触发超声波
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)  # 严格10us触发时序
    GPIO.output(TRIG_PIN, GPIO.LOW)

    # 3. 记录回声高电平持续时间
    pulse_start = 0
    pulse_end = 0

    # 等待ECHO高电平开始（带超时保护）
    start_time = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        if time.time() - start_time > TIMEOUT:
            print("⚠️  ECHO引脚超时（未检测到高电平）")
            return None
        pulse_start = time.time()

    # 等待ECHO高电平结束（带超时保护）
    start_time = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        if time.time() - start_time > TIMEOUT:
            print("⚠️  ECHO引脚超时（高电平持续过久）")
            return None
        pulse_end = time.time()

    # 4. 计算距离（往返路程÷2）
    pulse_duration = pulse_end - pulse_start
    distance = (pulse_duration * SOUND_SPEED) / 2

    # 过滤有效范围（2~400cm）
    if 2 <= distance <= 400:
        return round(distance, 2)
    else:
        print(f"⚠️  距离异常：{distance:.2f}cm（超出2~400cm范围）")
        return None

# ===================== 主函数 =====================
def main():
    # 检查是否为ROOT权限（必须）
    if os.geteuid() != 0:
        print("❌ 错误：必须以ROOT权限运行！")
        print("✅ 正确命令：sudo python3 hc_sr04.py")
        sys.exit(1)

    # 第一步：释放可能被占用的19/21引脚（核心修复）
    print("🔧 释放可能占用的GPIO引脚（19/21）...")
    release_gpio(TRIG_PIN)
    release_gpio(ECHO_PIN)
    time.sleep(0.2)

    # 注册Ctrl+C信号处理
    signal.signal(signal.SIGINT, signal_handler)
    
    # 第二步：初始化GPIO（增加重试机制）
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)  # 硬件引脚编号模式
    
    # 重试3次解决偶发的资源占用问题
    retry = 3
    while retry > 0:
        try:
            GPIO.setup(TRIG_PIN, GPIO.OUT, initial=GPIO.LOW)  # TRIG初始低电平
            GPIO.setup(ECHO_PIN, GPIO.IN)                     # ECHO设为输入
            break
        except OSError as e:
            retry -= 1
            print(f"❌ GPIO初始化失败，剩余重试次数：{retry} | 错误：{e}")
            time.sleep(0.5)
            release_gpio(TRIG_PIN)
            release_gpio(ECHO_PIN)
    else:
        print("❌ GPIO初始化失败，无法继续运行（请重启板卡后重试）")
        sys.exit(1)

    # 第三步：模块预热（关键）
    print("🔋 超声波模块预热中...（2秒）")
    time.sleep(2)

    # 打印启动信息
    print("="*60)
    print("✅ HC-SR04超声波测距程序启动（19/21引脚版）")
    print(f"   触发引脚(TRIG)：{TRIG_PIN} | 回声引脚(ECHO)：{ECHO_PIN}")
    print(f"   有效测距范围：2cm ~ 400cm | 按Ctrl+C退出")
    print("="*60)

    # 第四步：循环测距
    try:
        while True:
            distance = measure_distance()
            if distance is not None:
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 📏 测量距离：{distance} cm")
            else:
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ❌ 测距失败")
            time.sleep(MEASURE_INTERVAL)
    except Exception as e:
        print(f"\n❌ 程序异常：{e}")
    finally:
        # 最终清理GPIO资源
        print("\n🧹 程序退出，清理GPIO资源...")
        GPIO.cleanup()
        release_gpio(TRIG_PIN)
        release_gpio(ECHO_PIN)

# ===================== 程序入口 =====================
if __name__ == '__main__':
    main()
```