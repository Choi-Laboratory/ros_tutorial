#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String

def callback(message):
    rospy.loginfo("I heard message from %s.", message.data)

rospy.init_node('listener') #ノード名
print "waiting for massage..."
sub = rospy.Subscriber('chatter', String, callback)
rospy.spin()
