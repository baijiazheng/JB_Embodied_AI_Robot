Experiment: SLAM lidar mapping and Navigation

Goal: To master the SLAM modeling process and the slam_toolbox package.

Hardware: AuboRobot, computer.

Communication:  NoMachine

Input: lidar to the room.

Output: mapping and location -- SLAM . navigation -- NAV2

What I learned: SLAM is 'simultaneous localization and mapping' which is between mapping and location.
                NAV2 is the path planning navigation and chasiss controller.(avoid obstacle)
https://docs.nav2.org

# nav2 init: ${ROS_DISTRO} = humble; ${ROS_DISTRO}-devel = humble.
## echo $ROSDISTRO_INDEX_URL
# sudo apt install ros-${ROS_DISTRO}-navigation2 ros-${ROS_DISTRO}-nav2-bringup
# cd ~/nav2_ws/src
# git clone https://github.com/ros-planning/navigation2.git --branch ${ROS_DISTRO}-devel
# cd ~/nav2_ws
# rosdep install -y -r -q --from-paths src --ignore-src --rosdistro ${ROS_DISTRO}
# colcon build --symlink-install

# mapping:
# ros2 launch slam slam.launch.py
# ros2 launch slam rviz_slam.launch.py
# ros2 launch peripherals teleop_key_control.launch.py

# save map:
# cd ~/ros2_ws/src/slam/maps && ros2 run nav2_map_server map_saver_cli -f "map_01" --ros-args -p
# map_subscribe_transient_local:=true

# navigate
# ros2 launch navigation navigation.launch.py map:=map_01
# ros2 launch navigation rviz_navigation.launch.py