import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class CommandNode (Node):
	def __init__ (self):
		super().__init__('command_node')
		self.publisher_ = self.create_publisher(String
			,'robot_command'
			,10
		)
		self.timer = self.create_timer(2.0,self.send_command)
		self.commands = ["forward","left","stop","right","fly"]
		self.index = 0
	def send_command(self):
		msg = String()
		msg.data = self.commands[self.index]
		self.publisher_.publish(msg)
		self.get_logger().info(f"Send command:{msg.data}")
		self.index +=1
		if self.index >= len(self.commands):
			self.index = 0
def main(args=None):
	rclpy.init(args=args)
	node = CommandNode()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()
