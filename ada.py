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

        #c variable holds the read key from the keyboard
	c = 0


        #A and B variables hold the individual motor speeds out of 127
        speedA = 0
        speedB = 0

        #continuously loops through to read characters
	while True:

            #reads the character input from the keyboard and stores it in the c variable
	    c = stdscr.getch()                

            #if w is pressed go forward
	    if c == ord('w'):
                print('!A10', file=adausb)
                print('!b10', file=adausb)

            #if a is pressed go left
	    elif c == ord('a'):
                print('!a10', file=adausb)
                print('!b10', file=adausb)

            #if d is pressed go right
	    elif c == ord('d'):
                print('!A10', file=adausb)
                print('!B10', file=adausb)

            #if s is pressed go backward
	    elif c == ord('s'):
                print('!a10', file=adausb)
                print('!B10', file=adausb)

            #if z is pressed go forward AT LUDICROUS SPEED! (~%30 speed)
            elif c == ord('z'):
                print('!A40', file=adausb)
                print('!b40', file=adausb)

            #if anything else is pressed, pause the motors and reset the speed values
            else:
                print('%rrrrrr', file=adausb)
                speedA = 0
                speedB = 0

#calling of the previous function
arrowKeysControl()
