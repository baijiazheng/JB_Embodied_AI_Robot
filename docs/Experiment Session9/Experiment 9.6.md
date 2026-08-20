Experiment: Grasping control of Mobile Robot Based on Multimodal Large_scale Model (MLLM)

Goal: To master the multi-nodes interaction.

Hardware: AuboRobot

Communication: qwen-turbo

Input: the promote pycode and all nodes. filled with some location position message.

Output: listening and understanding the voice commands. pick and place smart like action group.

What I learned: The Multi_nodes are so complex that I should finish it on my Embodied Robot again.

# vim /home/sunrise/ros2_ws/src/large_models/large_models/config.py

# debug
# ros2 launch large_models_examples automatic_pick.launch.py debug:=pick
# ros2 launch large_models_examples automatic_pick.launch.py debug:=place

# launch
# ros2 launch large_models_examples vllm_navigation_transport.launch.py map:=map_01 enable_auto_calibration:=true