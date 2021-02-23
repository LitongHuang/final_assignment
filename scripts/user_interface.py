#! /usr/bin/env python

# import ros stuff
import rospy
from std_srvs.srv import *

# service callback
global pos
pos = [[-4,-3],[-4,-2].[-4,-7],[5,-7],[5,-3],[5,1]]

def set_new_pos(req):
    print("Target reached! Please insert a new position")

    while True :
       x = float(raw_input('x :'))
       y = float(raw_input('y :'))

       for a in range(6):
           if x == pos[a][0] and y == pos[a][1]:
               rospy.set_param("des_pos_x", x)
               rospy.set_param("des_pos_y", y)
               break
           else:
               print("The target position cannot be reached. Please insert a feasible position")
    return []


def main():
    rospy.init_node('user_interface')
    srv = rospy.Service('user_interface', Empty, set_new_pos)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        rate.sleep()


if __name__ == '__main__':
    main()
