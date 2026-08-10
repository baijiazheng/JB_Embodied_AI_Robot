Experiment:Bottom Board Data Interaction

Goal:To master the ROS2 package which is used to connect the STM32 Boaed with ROS2.

Hardware: STM32 Board, ROS2 Development Environment

Communication: UART/USB.Nomachine Used to connect the ROS2 with Computer.

Input:launched the ROS2 package and connected the STM32 Board with ROS2 using UART/USB. 
    Used Nomachine to establish a connection between the ROS2 environment and the computer.
    and read the data from /odom topic.
    and published the data to /cmd_vel topic to control the movement of the robot.

Output: The robot moves according to the commands published on the /cmd_vel topic.

What I learned: I learned how to use the ROS2 package to communicate with the STM32 Board and control the robot's movement.
and know how the launch files work for launching the ROS2 package.

# ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.4, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z:0.0}}" 