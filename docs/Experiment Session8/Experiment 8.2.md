Experiment: Lidar tracking object.

Goal: To master the usage of the lidar in ROS. To detect the info of lidar and realize the auto-tracking.

Hardware: Lidar(Robot), Computer

Communication: Nomachine

Input: give a moving object to Lidar

Output: Through the TOF and so on, there are function to feel the environment modle and motion.

What I learned: The lidar isn't affected by the so many factors including lightness. so it's good enough to be the main sensor to make robot touching the real world.

# ros2 launch example lidar_node.launch.py debug:=true
# tracking
# ros2 service call /lidar_app/enter std_srvs/srv/Trigger {}
# ros2 service call /lidar_app/set_running interfaces/srv/SetInt64 "{data: 2}"
# ros2 service call /lidar_app/set_param interfaces/srv/SetFloat64List "{data: [0.7, 60.0, 0.3]}"

# avoid the obstacle
# ros2 service call /lidar_app/enter std_srvs/srv/Trigger {}
# ros2 service call /lidar_app/set_running interfaces/srv/SetInt64 "{data: 1}"
# ros2 service call /lidar_app/set_param interfaces/srv/SetFloat64List "{data: [0.7, 60.0, 0.3]}"