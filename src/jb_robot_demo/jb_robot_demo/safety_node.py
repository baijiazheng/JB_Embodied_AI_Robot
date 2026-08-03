import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class SafetyNode(Node):
	def __init__(self):
		super().__init__('safety_node')
		self.subscription = self.create_subscription(String,
			'robot_command',
			self.command_callback,
			10)
		self.publisher = self.create_publisher(String,
			'safe_command',
			10)
		self.allowed_commands = ["forward","left","stop"]
	def command_callback(self,msg):
		command = msg.data
		self.get_logger().info(f"Check command:{command}")
		output = String()
		if command in self.allowed_commands:
			output.data = command
			self.get_logger().info("Command accepted")
		else:
			output.data= "stop"
			self.get_logger().warning("Command rejected!")
		self.publisher.publish(output)
def main(args = None):
	rclpy.init(args = args)
	node = SafetyNode()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()
if __name__ == "__main__":
	main()
