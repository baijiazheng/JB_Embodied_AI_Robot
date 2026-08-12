Experiment:AR(augmented Reality) Application Development

Goal: develop an AR application that can overlay virual objects onto the AprilTag detected in the real world.

Hardware: Camera, Computer

Communication: USB

Input: Image from camera

Output: Augmented image with virtual objects overlaid on detected AprilTags

What I learned: what is AR, how to use AR libraries to overlay virtual objects onto real-world images, and how to integrate AprilTag detection with AR applications.

# 启动 AR 基础功能节点
# cd ~
# ./start_ar.sh

# 启动/停止 AR 应用节点
# ros2 service call /ar/enter std_srvs/srv/Trigger "{}" 
# ros2 service call /ar/set_model interfaces/srv/SetString "data: 'bicycle'"
