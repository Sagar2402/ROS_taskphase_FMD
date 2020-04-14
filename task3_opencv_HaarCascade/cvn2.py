#! /usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

def callback(data):
    try:
        bridge=CvBridge()
        img=bridge.imgmsg_to_cv2(data, "8UC3")
        print(img)
        #print("HELLO")
        cv2.imshow('Image Window', img)
    except CvBridgeError as e:
        print(e)
    
    
    #cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.destroyAllWindows()

#cap.release()
    


def __init__():
    print("running")
    rospy.init_node('Node2')
    rospy.Subscriber('/image_raw', Image, callback)
    rospy.spin()

if __name__=='__main__':
    print("running")
    try:
        __init__()
    except rospy.RosInterruptionException:
        pass
