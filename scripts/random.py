#! /usr/bin/env python

import rospy
from std_srvs.srv import *

# service callback
global pos
pos = [[-4,-3],[-4,-2].[-4,-7],[5,-7],[5,-3],[5,1]]

def set_random(req)
    random_pos = random.randint(6)
    x = rospy.get_param("des_pos_x", pos[random_pos] [0])
    y = rospy.get_param("des_pos_y", pos[random_pos] [1])
    print("The random target position is: x = " +
          str(x) + ", y = " + str(y))
    return []

def main():
    rospy.init_node('random')
    srv = rospy.Service('random', Empty, set_random)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        rate.sleep()


if __name__ == '__main__':
    main()
