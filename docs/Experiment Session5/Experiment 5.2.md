Experiment:Based on the OpenCV library, QR code detection

Goal:build and test a QR code using the OpenCV library.

Hardware: OpenCV library, Camera

Communication: USB/Serial. Nomachine Used to connect the ROS2 with Computer.

Input:  build a QR code using qrcode library and print it.
        launch the ROS2 package and connected the camera.
        give the QR code to the camera.

Output: the QR code is detected.

What I learned: I learned how to use the qrcode and OpenCV library to detect QR codes in images captured by a camera.

# build a QR code using qrcode library and print it.
# cd ~/ros2_ws/src/example/example/qrcode
# python3 qrcode_creater.py

# ros2 launch peripherals depth_camera.launch.py
# source ~/track_env.sh
# python3 ~/ros2_ws/src/example/example/qrcode/qrcode_detecter.py