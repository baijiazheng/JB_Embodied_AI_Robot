Experiment:Based on Moveit2: Cartesian Path

Goal: 1. To master the method of Cartesian Path Planning which be able to realize linear motion of manipulator end-effector
      2. To understand the principle of path constraints which be able to generate smooth and collision-free trajectories in Cartesian space.

Hardware: Jetarm, upper computer

Communication: Nomachine

Input: the RViz's graphical selections

Output: stimulate the model like the programming. 

What I learned: Cartesian Path be used in the environment which is given with path.

# ros2 launch sdk jetarm_sdk.launch.py
# ros2 launch hiwonder_moveit_config demo.launch.py use_gazebo:=true use_sim_time:=true