Experiment:tracking objection based on deep camera.

Goal: To master the detection of color and the progress of jetarm moving.

Hardware: computer , auborobot

Communication: NoMachine.

Input: a colorful objection.

Output: tracking the objection.

What I learned: liking the experiment 7.2 , but the diffrence is not KCF but detect deffrence color.

# ros2 launch example color_track_node.launch.py

```
ros_robot_controller
        │
        │ /ros_robot_controller/imu_raw
        ▼
   imu_calib
        │
        │ /imu_corrected
        ▼
   imu_filter
        │
        │ /imu
        ▼
   ekf_filter_node
```