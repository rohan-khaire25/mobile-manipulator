#!/usr/bin/env python

import rospy
import actionlib
import sys
from std_msgs.msg import Bool
from mobile_manipulator_robot.msg import battery_simAction, battery_simGoal, battery_simResult

def battery_state(charge_condition):
    goal = battery_simGoal()
    goal.charge_state = charge_condition
    client.send_goal(goal)

if __name__ == "__main__":
    rospy.init_node('batterysimclient')
    client = actionlib.SimpleActionClient('mobile_manipulator_robot', battery_simAction) 
    client.wait_for_server()
    battery_state(int(sys.argv[1]))  
    client.wait_for_result