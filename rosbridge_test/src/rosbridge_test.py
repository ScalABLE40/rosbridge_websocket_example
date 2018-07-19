#!/usr/bin/env python

import rospy
import traceback
from rosbridge_test_class import ROSBridgeTest


if __name__ == "__main__":

    rospy.init_node('rosbridge_test')

    try:
        subscribing_topic = rospy.get_param('~subscribing_topic')
        publishing_topic = rospy.get_param('~publishing_topic')
    except Exception as e:
        raise KeyError('Unable to access ROS parameters')

    try:
        ROSBridgeTest = ROSBridgeTest(subscribing_topic, publishing_topic)
        rospy.spin()

    except Exception as e:
        rospy.logerr('[Wait Skill] Error: %s', str(e))
        rospy.logdebug(traceback.format_exc())
        quit()
