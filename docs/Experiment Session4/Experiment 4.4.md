Experiment:Voice Control Interaction

Goal:To master the voice control interaction with ROS2.

Hardware:ROS2 Development Environment, Microphone.

Communication: Serial.

Input:nature language voice 

Output:make the robot awake.

What I learned: I learned how to use the voice control interaction with ROS2 to make the robot awake. and how to use the microphone to capture natural language voice commands.

upload: ros2 launch xf_mic_asr_offline mic_init.launch.py enable_setting:=true 
        //haha,and I forgot to set the enable_setting:=true, so the robot can't awake.
run:    ros2 launch xf_mic_asr_offline mic_init.launch.py
test:   ros2 topic echo /awake_node/angle