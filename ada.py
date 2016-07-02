#!/usr/bin/env python

#This script is for the Penn State Robotics Club robot named Ada
#
#***Please remember to set the motor controller to any drive mode except for mixed channel***
#
#written by Geoffrey Billy
#last updated 6/23/16





#this library is used for outputting the motor command to the attached USB reciever
from __future__ import print_function

#this library is needed for reading multiple keys semicontinuous
import curses





#opens the USB serial connverter for writing to (sending commands to)
adausb = open('/dev/ttyUSB0', 'w')

#reset statement, used immediately after opening the USB device
print('%rrrrrr', file=adausb)





#function definition called later
def arrowKeysControl():

        #initalizes the keyboard to record the characters insput
	stdscr = curses.initscr()
	curses.cbreak()

        #s
	c = 0
        inc = 10
        speedA = 0
        speedB = 0

	while c != ord('q'):

	    c = stdscr.getch()                

	    if c == ord('w'):
#                if speedA < 100:
#                    speedA = speedA + inc
#                if speedB < 100:
#                    speedB = speedB + inc
                print('!A10', file=adausb)
                print('!b10', file=adausb)

            elif c == ord('z'):
#                if speedA < 100:
#                    speedA = speedA + inc
#                if speedB < 100:
#                    speedB = speedB + inc
                print('!A30', file=adausb)
                print('!b30', file=adausb)

	    elif c == ord('a'):
#                if speedA < 100:
#                    speedA = speedA + inc
#                if speedB > -100:
#                    speedB = spdd          eedB - inc
                print('!a10', file=adausb)
                print('!b10', file=adausb)

	    elif c == ord('d'):
#                if speedA > -100:
#                    speedA = speedA - inc
#                if speedB < 100:
#                    speedB = speedB + inc
                print('!A10', file=adausb)
                print('!B10', file=adausb)

	    elif c == ord('s'):
#                if speedA > -100:
#                    speedA = speedA - inc
#                if speedB > -100:
#                    speedB = speedB - inc
                print('!a10', file=adausb)
                print('!B10', file=adausb)

            else:
                print('%rrrrrr', file=adausb)
                speedA = 0
                speedB = 0

#calling of the previous function
arrowKeysControl()
