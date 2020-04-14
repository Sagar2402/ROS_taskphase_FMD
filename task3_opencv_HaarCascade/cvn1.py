#! /usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

face_cascade = cv2.CascadeClassifier('/home/sagar24/catkin_ws/src/beginner_tutorials/haarcascade_frontalface_default.xml')

bridge=CvBridge()
cap=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

rospy.init_node("Node1",anonymous=True)
pub=rospy.Publisher("/image_raw",Image,queue_size=10)
rate=rospy.Rate(10)

while cap.isOpened():
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    crop_img=img
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        crop_img = img[y:y+h, x:x+w]
    
    cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('img',600,600)    
    cv2.imshow('img',img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
    rate.sleep()
    rospy.loginfo(crop_img)
    ros_image=bridge.cv2_to_imgmsg(crop_img)
    pub.publish(ros_image)

cap.release()
cv2.destroyAllWindows()

#working
