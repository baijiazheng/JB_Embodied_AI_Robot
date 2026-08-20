Experiment: Line_follower!

Goal: To master the vision color detection.

Hardware: a color line, robot

Communication: Nomachine

Input: a color line in the camera vision.

Output: extract the color from the line. and follow it.

What I learned: the visiual line-follower is based on OpenCV, the core is to make the line in the middle of vision.

# ros2 launch example line_following_node.launch.py debug:=true
# ros2 service call /line_following/enter std_srvs/srv/Trigger {}
# ros2 service call /line_following/set_running std_srvs/srv/SetBool "{data: True}"