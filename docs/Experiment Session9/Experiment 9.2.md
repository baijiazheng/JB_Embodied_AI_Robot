Experiment: End-side VLM Deployment

Goal: To deploy the VLM to AuboRobot.

Hardware: Auborobot.

Communication: NoMachine.

Input: a picture or a sentence.

Output: describe the picture or generate drawing based on words.

What I learned: VLM can see, read, say and analyze all commands included the RGB imagine.
                InternLM2.5 is a nice VLM from china. light and quick.


# ros2 run hobot_llamacpp hobot_llamacpp --ros-args -p feed_type:=0 -p image:=config/image2.jpg -p image_type:=0 -p user_prompt:="描述一下这张图片." -p model_file_name:=vit_model_int16.hbm -p llm_model_name:=Qwen2.5-0.5B-Instruct-Q4_0.gguf