#!/usr/bin/env python



import rospy, sys, numpy as np
import geometry_msgs.msg
import moveit_msgs.msg
from std_msgs.msg import Header
from std_msgs.msg import Bool
from std_srvs.srv import Empty

def gripper_status(msg):
    if msg.data:
        return True
        # print('gripper status = {}'.format(msg.data))

def gripper_on():
    # Wait till the srv is available
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper1_on():
    # Wait till the srv is available
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper1/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper1/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper2_on():
    # Wait till the srv is available
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper2/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper2/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper3_on():
    # Wait till the srv is available
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper3/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper3/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper4_on():
    # Wait till the srv is available
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper4/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper4/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper5_on():
    # Wait till the srv is available
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper5/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper5/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper6_on():
    # Wait till the srv is available
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper6/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper6/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper7_on():
    # Wait till the srv is available
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper7/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper7/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper8_on():
    # Wait till the srv is available
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper8/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper8/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper9_on():
    # Wait till the srv is available
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper9/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper9/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e
        
def gripper10_on():
    # Wait till the srv is available
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper10/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper10/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper11_on():
    # Wait till the srv is available
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper11/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper11/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper12_on():
    # Wait till the srv is available
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper12/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper12/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper_off():
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper/off')
    try:
        turn_off = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper1_off():
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper1/off')
    try:
        turn_off = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper1/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper2_off():
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper2/off')
    try:
        turn_off = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper2/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper3_off():
    rospy.wait_for_service('/manipulator_completevacuum_gripper3/off')
    try:
        turn_off = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper3/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper4_off():
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper4/off')
    try:
        turn_off = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper4/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def gripper5_off():
    rospy.wait_for_service('/manipulator_complete/vacuum_gripper5/off')
    try:
        turn_off = rospy.ServiceProxy('/manipulator_complete/vacuum_gripper5/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

if __name__ == "__main__":
    try:
        rospy.init_node("ur5_gripper", anonymous=False)
        gripper_on()
        gripper1_on()
        gripper2_on()
        gripper3_on()
        gripper4_on()
        gripper5_on()
        gripper6_on()
        gripper7_on()
        gripper8_on()
        gripper9_on()
        gripper10_on()
        gripper11_on()
        gripper12_on()

    except rospy.ROSInterruptException:
        pass  
       




             