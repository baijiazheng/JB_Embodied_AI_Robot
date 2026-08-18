Experiment: RTAB-VSLAM mapping and navigation

Goal: To understand the basic original knowledge of VSLAM.
      To lauch the VSLAM mapping

Hardware: Lidar(Robot), Computer

Communication: Nomachine

Input: slowly move itself to mapping all thing with  VSLAM

Output: with vision and SLAM , the 3D bedroom modle was built slowly but perfectly.

What I learned: VSLAM is SLAM with the vision.

# ros2 launch slam rtabmap_slam.launch.py
# ros2 launch slam rviz_rtabmap.launch.py
# ros2 launch peripherals teleop_key_control.launch.py

# ros2 launch navigation rtabmap_navigation.launch.py
# ros2 launch navigation rviz_rtabmap_navigation.launch.py