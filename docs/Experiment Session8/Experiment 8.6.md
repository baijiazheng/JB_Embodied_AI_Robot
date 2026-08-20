Experiment: AuboRobot's sound source localization and following.

Goal: To master the method of using sound source localization, and robot adaptful motion.

Hardware: Robot.

Communication: Nomachine.

Input: the key words which can make xunfei awake.

Output: through the ACML, robot can locate the sound source.

What I learned: AMCL location can help fix the robotics location.still have problems waiting me.

# ros2 launch xf_mic_asr_offline sound_follower_move.launch.py
# ros2 service call /sound_follower/set_following std_srvs/srv/SetBool "{data: True}"