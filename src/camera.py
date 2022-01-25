#!/usr/bin/python3.8

import rospy
import cv2
from sensor_msgs.msg import Image	
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()

def imgCallback(data):
  cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
  cv2.imshow("Raw image", cv_image)
  cv2.waitKey(3)

def main():
  rospy.init_node('my_planner_node')
  img_sub = rospy.Subscriber("/camera/image_raw", Image, imgCallback)
  rospy.spin()

if __name__ == "__main__":
  main()

