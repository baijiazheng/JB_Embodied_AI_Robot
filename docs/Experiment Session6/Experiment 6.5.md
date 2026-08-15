Experiment: final: REAL and SIMULATION unite

Goal: To validate the validity of simulation experiment.

Hardware: Jetarm, upper computer, computer.

Communication: ROS2

Input: launch the controller node , and launch the MoveIt2 terminal.

Output: the real arm work like the simulation modle.and excute the same motion together.

What I learned: before launch the controller node, all commands are simulation.:(

problem: the real arm don't work together with simulation.
solution: change the robot_ros2_ws to the official ws.

# cd ~/ros2_ws && source install/setup.bash && ros2 launch ros_robot_controller ros_robot_controller.launch.py

# cd ~/ros2_ws && source install/setup.bash && ros2 launch moveit_config demo.launch.py