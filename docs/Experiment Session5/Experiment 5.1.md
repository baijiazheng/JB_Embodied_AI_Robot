Experiment:Based on the OpenCV library, color detection

Goal: To master the color detection

Hardware: OpenCV library, Camera

Communication: USB/Serial. Nomachine Used to connect the ROS2 with Computer.

Input:  launch the ROS2 package and connected the camera.
        give the color cube to the camera.

Output:the color of the cube is detected and displayed in the terminal.

What I learned: I learned how to use the OpenCV library to detect colors in images captured by a camera.

# connect the camera
# ros2 launch peripherals depth_camera.launch.py

# source ~/track_env.sh
# python3 ~/ros2_ws/src/example/example/color_detect/color_detect_demo.py