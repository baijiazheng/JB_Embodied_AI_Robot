import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class RobotStatusNode(Node):
	"""
	Robot status publisher node.
	"""
	
	def __init__(self):
		super().__init__('robot_status_node')
		
		self.publisher_ = self.create_publisher(
			String,
			'robot_status',
			10
		)
		self.timer = self.create_timer(
			1.0,
			self.publish_status
		)
		self.count = 0
	def publish_status(self):
		msg = String()
		msg.data = (
			f"Robot online | "
			f"heartbeat={self.count}"
		)
		self.publisher_.publish(msg)
		self.get_logger().info(
			msg.data
		)
		self.count += 1

def main(args=None):
	rclpy.init(args=args)
	node = RobotStatusNode()
	rclpy.spin(node)
	node.destory_node()
	rclpy.shutdown()
if __name__ == '__main__':
	main()
