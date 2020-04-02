#! /usr/bin/env python
import rospy
from beginner_tutorials.msg import Num
 
def talker():
    pub = rospy.Publisher('topic1', Num)
    rospy.init_node('custom_talker', anonymous=True)
    r = rospy.Rate(10) #10hz
    msg = Num()
    msg.name = "Sagar Pathak"
    msg.age = 20

    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass

