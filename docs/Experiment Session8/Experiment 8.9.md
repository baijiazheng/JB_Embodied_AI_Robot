Experiment: Voice controlled Multi-Point Navigation 

Goal: To master the influence every nodes working.

Hardware: AuboRobot

Communication: NoMachine

Input: Voice about the command which point the beginning and finish position.

Output: compute and complete the motion based on navigation info.

What I learned: this is a perfect study plateform to understand how different nodes can work together.

# ros2 launch xf_mic_asr_offline voice_control_navigation_transport.launch.py map:=map_01

# edit A point (use 'i' enter, use ESC+':wq' save and quit)
# vim ./ros2_ws/src/xf_mic_asr_offline/scripts/voice_control_navigation.py

# ~/ros2_ws/.stop_ros.sh