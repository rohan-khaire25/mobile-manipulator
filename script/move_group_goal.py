#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import actionlib
import geometry_msgs.msg
from std_srvs.srv import Empty

def simple_pick_place():
  ## First initialize moveit_commander and rospy.
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node('simple_pick_place',
                  anonymous=True)

  ## Instantiate a MoveGroupCommander object.  This object is an interface
  ## to one group of joints.  In this case the group refers to the joints of
  ## robot1. This interface can be used to plan and execute motions on robot1.
  robot1_group = moveit_commander.MoveGroupCommander("arm")
  scene = moveit_commander.PlanningSceneInterface()
  robot = moveit_commander.RobotCommander()
  
  ## Action clients to the ExecuteTrajectory action server.
  robot1_client = actionlib.SimpleActionClient('execute_trajectory',
    moveit_msgs.msg.ExecuteTrajectoryAction)
  robot1_client.wait_for_server()
  rospy.loginfo('Execute Trajectory server is available for arm')

  ## Set a named joint configuration as the goal to plan for a move group.
  ## Named joint configurations are the robot poses defined via MoveIt! Setup Assistant.
  robot1_group.set_named_target("straight_up")

  ## Plan to the desired joint-space goal using the default planner (RRTConnect).
  plan = robot1_group.plan()
  ## Create a goal message object for the action server.
  robot1_goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
  ## Update the trajectory in the goal message.
  robot1_goal.trajectory = plan

  ## Send the goal to the action server.
  robot1_client.send_goal(robot1_goal)
  robot1_client.wait_for_result()

  robot1_group.set_named_target("pre_grasp")

  plan = robot1_group.plan()
  robot1_goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
  robot1_goal.trajectory = plan

  robot1_client.send_goal(robot1_goal)
  robot1_client.wait_for_result()

  rospy.sleep(5)

  waypoints = []
  # start with the current pose
  current_pose = robot1_group.get_current_pose()
  rospy.sleep(0.5)
  current_pose = robot1_group.get_current_pose()

  ## create linear offsets to the current pose
  new_eef_pose = geometry_msgs.msg.Pose()

  # Manual offsets because we don't have a camera to detect objects yet.
  new_eef_pose.position.x = current_pose.pose.position.x 
  new_eef_pose.position.y = current_pose.pose.position.y + 0.05
  new_eef_pose.position.z = current_pose.pose.position.z 

  # Retain orientation of the current pose.
  new_eef_pose.orientation = copy.deepcopy(current_pose.pose.orientation)

  waypoints.append(copy.deepcopy(new_eef_pose))



  new_eef_pose.position.z = current_pose.pose.position.z - 0.04
  waypoints.append(copy.deepcopy(new_eef_pose))
  
  #new_eef_pose.position.z = current_pose.pose.position.z + 0.06
  #waypoints.append(copy.deepcopy(new_eef_pose))
  

  ## We want the cartesian path to be interpolated at a resolution of 1 cm
  ## which is why we will specify 0.01 as the eef_step in cartesian
  ## translation.  We will specify the jump threshold as 0.0, effectively
  ## disabling it.
  fraction = 0.0
  for count_cartesian_path in range(0,3):
    if fraction < 1.0:
      (plan_cartesian, fraction) = robot1_group.compute_cartesian_path(
                                   waypoints,   # waypoints to follow
                                   0.01,        # eef_step
                                   0.0)         # jump_threshold
    else:
      break

  robot1_goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
  robot1_goal.trajectory = plan_cartesian

  robot1_client.send_goal(robot1_goal)
  robot1_client.wait_for_result()

  rospy.sleep(5)

  robot1_group.set_named_target("grasp_pose")

  plan = robot1_group.plan()
  robot1_goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
  robot1_goal.trajectory = plan

  robot1_client.send_goal(robot1_goal)
  robot1_client.wait_for_result()

  ## When finished shut down moveit_commander.
  moveit_commander.roscpp_shutdown()

if __name__=='__main__':
  try:
    simple_pick_place()
  except rospy.ROSInterruptException:
    pass  
