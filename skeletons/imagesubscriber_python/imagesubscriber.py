#!/usr/bin/env python
import roslib; roslib.load_manifest('imagesubscriber_python')
import rospy
from sensor_msgs.msg import Image
import numpy as np
import cv2
import cv2.cv as cv # to avoid using opencv1 version of python
from cv_bridge import CvBridge, CvBridgeError

class Node:

  def __init__(self):
    self.pub = rospy.Publisher('image_out', Image)
    self.sub = rospy.Subscriber('image_in', Image, self.imgCb)
    self.bridge = CvBridge()

  def imgCb(self, data):
    cvImage = np.asarray(self.bridge.imgmsg_to_cv(data, "bgr8"))
    imageResult = imageOperation(cvImage)
    self.pub.publish(self.bridge.cv_to_imgmsg(cv.fromarray(imageResult), "bgr8"))

  def imageOperation(image):
    # do something with the image
    return image


if __name__ == '__main__':
  sd = Node()
  rospy.init_node('nodeskeleton')
  rospy.spin()
