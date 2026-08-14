Experiment: MoveIt2:collision checking

Goal: To understand the influence of Allowed Collision Matrix (ACM).

Hardware: Jetarm , computer.

Communication: Nomachine

Input: Tick the Collision-aware IK selection.and design a scene objection beteween beginner and final pose.

Output: use Joint1 to make the jetarm leaving the obstacle far away.

What I learned: ACM is used to optimize collision-detection efficiency.(avoid the 'allow_collision=TRUE' situation occupy the CPU)
                CollisionWorld 's Flexible Collision Library (FCL) give the easy computation.

# ros2 launch sdk jetarm_sdk.launch.py
# ros2 launch hiwonder_moveit_config demo.launch.py use_gazebo:=true use_sim_time:=true