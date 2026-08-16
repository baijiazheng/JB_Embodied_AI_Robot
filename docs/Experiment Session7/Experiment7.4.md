Experiment: Colorful object Identification and Sorting.

Goal: To master the colorful object detection based on 2D Vision.

Hardware: Computer , AuboRobot

Communication: USB.

Input: In region of interest (ROI), place colorful objects.
        ROI can change by wsda. 

Output: Perform LAB binarization on ROI. then grab and place blocks of different colors.

What I learned: The LAB color space segmentation is the important method to filter the obstacle about light.

# source ~/track_env.sh 
# ros2 launch example color_sorting_node.launch.py debug:=true
# ros2 launch example color_sorting_node.launch.py