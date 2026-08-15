Experiment:MoveIt2: scene design

Goal: TO master how to realize scene design.

Hardware: jetarm , computer

Communication: NoMachine

Input: scene design with provided modle.

Output: keep computing until a valid path is found.

What I learned: The scene design function is aiming to support stimulation for robot test virtually. RViz is godness.

# ros2 launch sdk jetarm_sdk.launch.py
# ros2 launch moveit_config demo.launch.py use_gazebo:=true use_sim_time:=true