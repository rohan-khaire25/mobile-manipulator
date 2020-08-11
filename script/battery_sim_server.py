#!/usr/bin/env python

import time
import rospy
import actionlib
from std_msgs.msg import Int32, Bool
from multiprocessing import Process
from mobile_manipulator_robot.msg import battery_simAction, battery_simGoal, battery_simResult, battery_simFeedback

def batterysim():
    battery_level = 100
    result = battery_simResult()
    while not rospy.is_shutdown():
            if rospy.has_param("/MyRobot/BatteryStatus"):
                time.sleep(1)
                param = rospy.get_param("/MyRobot/BatteryStatus")
                if param == 1:
                    if battery_level == 100:
                        result.battery_status = "FULL"
                        server.set_succeeded(result)
                        break
                    else:
                        battery_level += 1
                        rospy.loginfo("charging..currently, %s", battery_level)
                        time.sleep(4)
                elif param == 0:
                    battery_level -= 1
                    rospy.logwarn("discharging..currently, %s", battery_level)
                    time.sleep(2)

def goalfun(goal):
    rate = rospy.Rate(2) 
    process = Process(target=batterysim)
    process.start()
    time.sleep(1)
    if goal.charge_state == 0:
        rospy.set_param("/MyRobot/BatteryStatus", goal.charge_state)
    if goal.charge_state == 1:
        rospy.set_param("/MyRobot/BatteryStatus", goal.charge_state)    

if __name__ == '__main__':
    rospy.init_node('batterysimserver')     
    server = actionlib.SimpleActionServer('mobile_manipulator_robot', battery_simAction, goalfun, False)  
    server.start()
    rospy.spin() 
