Experiment:MoveIt2 Kinematics and Motion Planning

Goal:   To master the kinematics and motion planning techniques using MoveIt2.
        To master the forward and inverse kinematics techniques, and master geometric method and DH parameter modeling for solving joint angles.
        To master MoveIt2 path-planning and control methods to realize accurate movement of jetarm to the specified position.


Hardware: Computer with ROS2 and MoveIt2 installed, and a robotic arm (jetarm)

Communication: USB

Input: Joint angles/ desired end-effector position and orientation,

Output: Planned path, joint trajectories and movement of the robotic arm to the specified position.

What I learned: How confident the MoveIt2 work in ROS2.

problem: the jetarm don't work like the simulation.and don't display the real position and orientation in rviz2.
solution: research the action if not work as usual.
        Through all detection, i know there are because of only simulation.

# ros2 launch sdk jetarm_sdk.launch.py
# ros2 launch moveit_config demo.launch.py use_gazebo:=true use_sim_time:=true