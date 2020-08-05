#!/usr/bin/env python

import rospy
import actionlib
from std_msgs.msg import Float64
from trajectory_msgs.msg import JointTrajectoryPoint
from control_msgs.msg import JointTrajectoryAction, JointTrajectoryGoal, FollowJointTrajectoryAction, FollowJointTrajectoryGoal

def move_joint(angles):
    goal = FollowJointTrajectoryGoal()
    goal.trajectory.joint_names = ['arm_base_joint', 'shoulder_joint', 'bottom_wrist_joint', 'elbow_joint', 'top_wrist_joint']
    point = JointTrajectoryPoint()
    point.positions = angles
    point.time_from_start = rospy.Duration(3)
    goal.trajectory.points.append(point)
    client.send_goal_and_wait(goal)

if __name__ == '__main__':
    rospy.init_node('joint_position_test')
    client = actionlib.SimpleActionClient('arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
    client.wait_for_server()
    move_joint([-1.57, 0.2101, 0.0227, 0.0024,1.5124])