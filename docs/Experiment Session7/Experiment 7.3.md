Experiment: Besed on mediaPipe's hand gesture, hand tracking.

Goal: know how it works.

ardware: Robot. computer.

Communication: NoMachine. USB.

Input: give the hand to the camera.

Output:Though the second-time detection, output the servo_position to the topic which is subscribed by controller_manage or kinematics.

What I learned: The MediaPipe is enough efficient algrithm to detect the hand gesture.

# source ~/track_env.sh && ros2 launch example hand_track_node.launch.py