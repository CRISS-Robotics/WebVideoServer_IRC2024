#!/usr/bin/env python3

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def publish_camera_image():
    rospy.init_node('camera_node', anonymous=True)
    rate = rospy.Rate(10)  # 10 Hz

    cap = cv2.VideoCapture(0)  # Use the default camera (change as needed)
    bridge = CvBridge()
    pub = rospy.Publisher('/image_raw', Image, queue_size=10)

    while not rospy.is_shutdown():
        ret, frame = cap.read()

        if ret:
            # Convert the OpenCV image to a ROS image message
            img_msg = bridge.cv2_to_imgmsg(frame, "bgr8")
            pub.publish(img_msg)

        rate.sleep()

    cap.release()

if __name__ == '__main__':
    try:
        publish_camera_image()
    except rospy.ROSInterruptException:
        pass
