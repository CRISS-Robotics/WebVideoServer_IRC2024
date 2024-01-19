Create your catkin workspace and add the contents of this repo in the src folder. Run catkin_make.
Follow the steps below to test the code-
1) Start the ros master in 1st terminal- roscore
2) In 2nd terminal, run the ros node to publish the camera feed to the image_raw topic- rosrun my_camera_pkg camera_node.py
3) In a 3rd terminal, run the code to start the web video server- rosrun web_video_server web_video_server
4) Check the feed on localhost:8080 (or if you want to check on any other device connected to the same network, use the laptop's ip address instead of localhost)
5) Make sure to run 'source devel/setup.bash' in every new terminal before running the packages.

(Step 2 is for testing only)

Important links:
-git repo link: https://github.com/Intelligent-Quads/iq_tutorials/blob/master/docs/web_video_server.md
-video explaination: https://www.youtube.com/watch?v=bh9mKgiIJAk
