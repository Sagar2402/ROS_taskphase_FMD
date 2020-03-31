#! /usr/bin/env python
import rospy
from beginner_tutorials.msg import Num
from beginner_tutorials.msg import Num2

data2=Num2()

def callback(data):
    data2.name = data.name    
    if data.age<18 :
        data2.eli="Ineleigible"
    elif data.age>=18 :
        data2.eli="Eligible"
    print(data)


rospy.init_node('custom_talker2', anonymous=True)
sub = rospy.Subscriber("topic1", Num, callback)
pub = rospy.Publisher('topic2', Num2, queue_size=1)


rospy.loginfo(data2)
pub.publish(data2)
print('done')    
rospy.spin()
