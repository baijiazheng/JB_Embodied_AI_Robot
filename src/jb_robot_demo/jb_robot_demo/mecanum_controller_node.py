import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

class MecanumControllerNode(Node):
    def __init__(self):
        super().__init__('mecanum_controller_node')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.cmd_vel_callback,
            10
        )
        self.subscription  # prevent unused variable warning
        self.publisher_ = self.create_publisher(Twist,'motor_cmd',10)

    def cmd_vel_callback(self, msg):
        linear_velocity = msg.linear.x
        angular_velocity = msg.angular.z
        self.get_logger().info(f'Received cmd_vel: linear={linear_velocity}, angular={angular_velocity}')

        left_motor_speed = linear_velocity - angular_velocity
        right_motor_speed = linear_velocity + angular_velocity

        left_motor_msg = Twist()
        left_motor_msg.linear.x = left_motor_speed
        self.publisher_.publish(left_motor_msg)
        self.get_logger().info(f'Published left motor speed: {left_motor_speed}')

        right_motor_msg = Twist()
        right_motor_msg.linear.x = right_motor_speed
        self.publisher_.publish(right_motor_msg)
        self.get_logger().info(f'Published right motor speed: {right_motor_speed}')
def main(args=None):
    rclpy.init(args=args)
    node = MecanumControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()