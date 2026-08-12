Experiment:AprilTag: Based on the OpenCV library, AprilTag detection

Goal: Detect AprilTag using the OpenCV library.

Hardware: Camera, Computer

Communication: USB

Input: Image from camera

Output: Detected AprilTag positions and IDs

What I learned: AprilTag detection is a robust method for identifying fiducial markers in images. The OpenCV library provides a convenient implementation for this task.

# ros2 launch peripherals depth_camera.launch.py

# source ~/track_env.sh
# python3 ~/ros2_ws/src/example/example/apriltag/apriltag_discern.py