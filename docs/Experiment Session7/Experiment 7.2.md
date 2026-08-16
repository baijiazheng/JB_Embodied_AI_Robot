Experiment: Kernelized Correlation Filter (KCF) object tracking

Goal: To learn about the base definition of the KCF algorithm.
      To master the object tracking based on KCF.

Hardware: Robot. computer.

Communication: NoMachine. USB.

Input: give the object to the camera.

Output: camera with KCF algorithm detected the object . and PID change the y label and xlabel number.

What I learned: The KCF algorithm is a repo about core-found. which is important and efficient to find tracker. 

# source ~/track_env.sh
# ros2 launch example kcf_track_node.launch.py


# echo "MACHINE_TYPE=$MACHINE_TYPE"
# export MACHINE_TYPE=aubomove_Mecanum / nano ./bashrc
```
Question:
Does /joint_states exist?

        ↓

If NO
    find publisher

If YES
    inspect message

        ↓

Is timestamp fresh?

        ↓

Are joint names correct?

        ↓

Does MoveIt receive them?
```
```
                  Camera
                    │
                    ▼
        /depth_cam/rgb/image_raw
                    │
                    ▼
                /kcf_track

                    │
                    ▼
          ServosPosition

                    │
          ┌─────────┴─────────┐
          │                   │
/controller_manager        Kinematics
          |                   |
          │                   │
          └─────────┬─────────┘
                    │
                    ▼
                Robot Arm
```

```
debug progress

Kinematics error
 ↓ so many test,confirm the architecture
kcf_track
 ↓
/kinematics/init_finish
 ↓
kinematics node
 ↓
Python import
 ↓
inverse_kinematics.so
 ↓
transform.base_link
 ↓
MACHINE_TYPE
 ↓
JetRover_Mecanum ≠ aubomove_Mecanum
```