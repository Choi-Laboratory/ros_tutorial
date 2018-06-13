#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import socket
import time
from std_msgs.msg import String

rospy.init_node('talker')
pub = rospy.Publisher('chatter', String, queue_size=1)

#ホスト名(自分のPC名)を取得
hostname = String()
hostname.data = socket.gethostname()
print "your hostname: " + str(hostname.data)
time.sleep(1)

#1秒に1回自分のPC名を送信
rate = rospy.Rate(1)
time = 1
while not rospy.is_shutdown():
    data = str(hostname.data) + ", time:"+str(time)
    pub.publish(data)
    rospy.loginfo("published data. time:"+str(time))
    time += 1
    rate.sleep()
