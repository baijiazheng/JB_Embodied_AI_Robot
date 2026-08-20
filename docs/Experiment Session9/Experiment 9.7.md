Experiment: Visiual tracking based on MLLM

Goal: To master the method of detection and tracking with pointed objection.

Hardware: AuboRobot

Communication: step

Input: tell the robot what you want to track

Output: the robot will PID tracking the objection which you speak about.

What I learned: This is the final experiment but it's my door to the new world. when i finish the complete all experiment again with my hands, i will remember the night -- 2:43--don't excited and not actual experiment but know YOLO and OpenCV work together. I will master these all experiment after later.

# ros2 launch large_models_examples vllm_track.launch.py

# fix
# ros2 launch large_models_examples vllm_track.launch.py wakeup_confidence:=800

# ~/ros2_ws/.stop_ros.sh