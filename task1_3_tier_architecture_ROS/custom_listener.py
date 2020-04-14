#! /usr/bin/env python
import rospy
from beginner_tutorials.msg import Num2

def callback2(data):
    rospy.loginfo("%s is %s" % (data.name, data.eli))
    
def listener():

    rospy.init_node('custom_listener', anonymous=True)

    sub = rospy.Subscriber('topic2', Num2, callback2)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    print "running"
    listener()
