Experiment: End-side LLM Deployment

Goal: To deploy LLM in Robot.

Hardware: AuboRobot.

Communication: Nomachine

Input: chat with DeepseekR1 based on QWen B1.5

Output: so fast to respond with nice nature Chinese

What I learned: The LLM should run in so much ION memory space.

# max the ION memory space
# sudo /usr/hobot/bin/hb_switch_ion.sh bpu_first
# reboot

# source /opt/tros/humble/setup.bash

# lib=/opt/tros/humble/lib/hobot_xlm/lib
# export LD_LIBRARY_PATH=${lib}:${LD_LIBRARY_PATH}
# cp -r /opt/tros/humble/lib/hobot_xlm/config/ .
# ros2 run hobot_xlm hobot_xlm --ros-args -p feed_type:=0 -p model_name:="DeepSeek_R1_Distill_Qwen_1.5B"

# refresh avoiding the other influence
# sudo /usr/hobot/bin/hb_switch_ion.sh default
# reboot