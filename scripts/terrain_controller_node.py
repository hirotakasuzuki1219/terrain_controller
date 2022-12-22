#!/usr/bin/env python                                                           
import rospy
from terrain_controller.msg import terrain_msgs
from datetime import datetime

def terrain_publisher():
    d = terrain_msgs()
    d.terrain_heightmap_ros = [0] * 100
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():

        d.terrain_heightmap_ros[10]=1
        d.terrain_heightmap_ros[20]=2
        d.terrain_heightmap_ros[30]=3
        now = datetime.now()

        pub.publish(d)
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('terrain_pub')
    pub = rospy.Publisher('terrain_heightmap', terrain_msgs , queue_size=1)
    terrain_publisher()
    rospy.spin()