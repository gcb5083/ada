#!/usr/bin/env python

#This script is for the Penn State Robotics Club robot named Ada
#
#***Please rmemeber to set the motor controller to any drive mode except for mixed channel***
#
#written by Geoffrey Billy
#last updated 6/23/16



from __future__ import print_function
import curses



controls = '\t1: Arrow Keys\t2: Trackpad (broken)\t3: Mouse (unimplemented)\t'

adausb = open('/dev/ttyUSB0', 'w')
print('%rrrrrr', file=adausb)



def controlSelection():

	source = raw_input('Enter one of the following choices for the selected control scheme.' + controls)

	while True:

		if source == str(1):
			arrowKeysControl()

		elif source == str(2):
			mouseTrackpadControl(0)

		elif source == str(3):
			mouseTrackpadControl(1)

		else:
			source = raw_input('Please re-enter your selection.' + controls)

                source == "reset"



def arrowKeysControl():

	stdscr = curses.initscr()
	curses.cbreak()

	c = 0
        speedA = 0
        speedB = 0

	while c != ord('q'):

	    c = stdscr.getch()                

	    if c == ord('w'):
                print(changeSpeed(speedA, 'A', 10), file=adausb)
                if speedA < 100:
                    speedA = speedA + 10
                print(changeSpeed(speedB, 'B', 10), file=adausb)
                if speedB < 100:
                    speedB = speedB + 10
 
	    elif c == ord('a'):
                print(changeSpeed(speedA, 'A', 5), file=adausb)
                if speedA < 100:
                    speedA = speedA + 5
                print(changeSpeed(speedB, 'B', -5), file=adausb)
                if speedB > -100:
                    speedB = speedB - 5

	    elif c == ord('d'):
                print(changeSpeed(speedA, 'A', -5), file=adausb)
                if speedA > -100:
                    speedA = speedA - 5
                print(changeSpeed(speedB, 'B', 5), file=adausb)
                if speedB < 100:
                    speedB = speedB + 5

	    elif c == ord('s'):
                print(changeSpeed(speedA, 'A', -10), file=adausb)
                if speedA > -100:
                    speedA = speedA - 10
                print(changeSpeed(speedB, 'B', -10), file=adausb)
                if speedB > -100:
                    speedB = speedB - 10

            else:
                print('%rrrrrr', file=adausb)



def changeSpeed(speed, motor, increment):

        speed = speed + increment

        if speed >= 0:
            return ('!' + motor + str(speed))

        else:
            if ord(motor) == ord('A'):
                return ('!a' + str(abs(speed)))

            else:
                return ('!b' + str(abs(speed)))



def mouseTrackpadControl(nn):
	mouse = file('/dev/input/mouse' + str(nn))
	while True:
		d, dx, dy = tuple(ord(c) for c in mouse.read(3))
		print(str(dx) + '\t' + str(dy))
		if dx > 127:
			dx = (dx - 256)
		if dy > 127:
			dy = (dy - 256)
		if abs(dx) > abs(dy) + 1:
			if dx > 0:
				print('!B40', file=adausb)
			else:
				print('!b40', file=adausb)
		elif abs(dx) + 1 < abs(dy):
			if dy > 0:
				print('!A40', file=adausb)
			else:
				print('!a40', file=adausb)
		else:
			print('%rrrrrr', file=adausb)



controlSelection()
