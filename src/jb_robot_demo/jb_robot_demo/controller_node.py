import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RobotController(Node):
	def __init__(self):
		super().__init__('controller_node')
		self.subsciption = self.create_subscription(String,
			'safe_command',
			self.command_callback,
			10
		)
		self.publisher = self.create_publisher(String,
			'robot_status',
			10
		)
		self.current_state = 'idle'
	def command_callback(self,msg):
		command = msg.data
		self.get_logger().info(f"Receive command:{command}")
		if command == 'forward':
			self.current_state = "moving forward"
		elif command == 'left':
			self.current_state = "turning left"
		elif command == "stop":
			self.current_state = "stopped"
		status_msg = String()
		status_msg.data = self.current_state
		self.publisher.publish(status_msg)
def main(args = None):
	rclpy.init(args = args)
	node = RobotController()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()
