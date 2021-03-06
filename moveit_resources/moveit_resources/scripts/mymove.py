#! /usr/bin/env python3
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from geometry_msgs.msg import Twist

  
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_tut',anonymous=True)

robot=moveit_commander.RobotCommander()
scene=moveit_commander.PlanningSceneInterface()
group=moveit_commander.MoveGroupCommander("robotic_arm")
display_trajectory_publisher=rospy.Publisher('/arm/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=10)
joints=rospy.wait_for_message("/arm/inverse_kin",Twist)
#pose_target=geometry_msgs.msg.Pose()
#pose_target.orientation.w=1.0
#pose_target.position.x=0.009
#pose_target.position.y=0.0
#pose_target.position.z=0.1
#group.set_pose_target(pose_target)
group.set_planning_pipeline_id("chomp")
#group.set_planner_id("RRT")
group.set_planning_time(5)
#print(group.get_current_joint_values())

group.set_num_planning_attempts(10)
#rospy.loginfo(group.get_planning_pipeline_id())
#plan1=group.plan()
#print(plan1[0])
print(joints)
group.go([0.0,23.0,0.0,0.0,0.0])
#group.go([joints.linear.x,joints.linear.y,joints.linear.z,joints.angular.x,2.0])
#rospy.sleep(2)
#group.go([0.0,0.0,0.0,0.0,0.0])
rospy.sleep(5)

moveit_commander.roscpp_shutdown()
