#!/usr/bin/python
import numpy as np
import rospy
from std_msgs.msg import Empty
pub_land = rospy.Publisher('bebop/land',Empty,queue_size=10)
rospy.init_node('talker')
rate = rospy.Rate(10)
for i in range(20):
	pub_land.publish()
	rate.sleep()
