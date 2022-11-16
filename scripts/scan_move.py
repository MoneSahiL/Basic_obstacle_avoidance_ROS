#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


def callback(msg):
    #print(len(msg.ranges))
    dist = 1
    fwd = msg.ranges[180]
    lft = msg.ranges[359]
    rgt = msg.ranges[0]
    if fwd > dist:
        vel_msg.linear.x = 0.01
        vel_msg.angular.z = 0.0
    if fwd < dist:
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0.01
    if lft < dist:
        vel_msg.angular.z = -0.01
    if rgt < dist:
        vel_msg.angular.z = 0.01

    vel_pub.publish(vel_msg)


rospy.init_node('scan_move_node')
vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
vel_msg = Twist()
scan_sub = rospy.Subscriber('/scan', LaserScan, callback)

rate = rospy.Rate(1)

rospy.spin()

