Experiment: Robot hand gestures controller.

Goal: To realize the config hand gesture to control the robot motion.

Hardware: AuboRobot.

Communication: NoMachine.

Input: hand gestures which be confignited.

Output: Robot move like the gesture.

What I learned: angle is the control's core for detect commands.

# source ~/python_envs/opencv-env/bin/activate
# ros2 launch example hand_gesture_control_node.launch.py

# ros2 topic echo/servo_controller