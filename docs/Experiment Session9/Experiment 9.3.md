Experiment: End-side instance segmentation accelerated by BPU

Goal: To master the segmentation by YOLOv8_Seg.

Hardware: Auborobot

Communication: Nomachine

Input: a picture

Output: using so many algorithm to get out a perfect segmentatial callback.

What I learned: Yolo V8 is using the marix compute which is BPU allowed for. so it's a important thinking direction.

# source /opt/tros/humble/setup.bash
# ros2 launch dnn_node_example dnn_node_example_feedback.launch.py dnn_example_config_file:=config/yolov8segworkconfig.json dnn_example_image:=config/test.jpg