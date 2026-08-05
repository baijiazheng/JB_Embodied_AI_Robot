import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

class CMDVelNode (Node):
        def __init__ (self):
                super().__init__('cmd_vel_node')
                self.publisher_ = self.create_publisher(Twist
                        ,'cmd_vel'
                        ,10
                )
                self.timer = self.create_timer(2.0,self.send_command)
                self.commands = ["forward","left","stop","right"]
                self.index = 0
        def send_command(self):
                msg = Twist()
                command = self.commands[self.index]
                if command == "forward":
                        msg.linear.x = 0.5
                        msg.angular.z = 0.0
                elif command == "left":
                        msg.linear.x = 0.0
                        msg.angular.z = 0.5
                elif command == "right":
                        msg.linear.x = 0.0
                        msg.angular.z = -0.5
                else:  # stop
                        msg.linear.x = 0.0
                        msg.angular.z = 0.0
                self.publisher_.publish(msg)
                self.get_logger().info(f"Send velocity command:{command}")
                self.index +=1
                if self.index >= len(self.commands):
                        self.index = 0
def main(args=None):
        rclpy.init(args=args)
        node = CMDVelNode()
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
        main()

