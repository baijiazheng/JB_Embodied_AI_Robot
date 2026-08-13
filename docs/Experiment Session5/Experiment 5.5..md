Experiment: Background segmentation Based on MediaPipe

Goal: To master the background ssegmentation technique using MediaPipe.

Hardware: Laptop with webcam

Communication: USB

Input: Video stream from webcam

Output: Segmented image with background removed

What I learned: MediaPipe is a powerful framework that allows for real-time background segmentation in video streams. By leveraging its pre-trained models, I was able to effectively separate the subject from the background in live video feeds. This technique can be applied in various applications such as virtual backgrounds for video conferencing, augmented reality, and content creation. I also learned about the importance of lighting and camera positioning to achieve optimal segmentation results.

# ros2 launch peripherals depth_camera.launch.py

# source ~/track_env.sh
# python3 ~/ros2_ws/src/example/example/mediapipe_example/self_segmentation.py