#!/usr/bin/python3.8

import rospy
import cv2
from sensor_msgs.msg import Image	
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

bridge = CvBridge()
low = np.array( [0 , 50, 50] )
high = np.array( [10, 255, 255] )

def imgCallback(data):
  cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
  hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
  red_image = cv2.inRange(hsv, low, high )
  cv2.imshow("Raw image", red_image)
  cv2.waitKey(3)

def main():
  
  rospy.init_node('my_planner_node')
  img_sub = rospy.Subscriber("/camera/image_raw", Image, imgCallback)
  rospy.spin()

if __name__ == "__main__":
  main()

