Experiment:Servo Control Interaction

Goal:control the servo motors.

Hardware: Servo Motors, Microcontroller

Communication: Nomachine.

Input: Position commands for the servo motors.

Output: Servo motors move to the specified positions.

What I learned:how to control servo motors using position commands and how to interface with the microcontroller to send these commands.

# ros2 topic pub /ros_robot_controller/bus_servo/set_position ros_robot_controller_msgs/msg/ServosPosition '{"position": [{"id": 1, "position": 700}]}'