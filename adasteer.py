#!/usr/bin/env python

#This is the second script written for the Penn State Robotics Club robot named Ada
#
#***Please remember to set the motor controller to MIXED CHANNEL drive mode***
#
#written by Geoffrey Billy
#last updated 7/1/16


from __future__ import print_function
import curses


adausb = open('/dev/ttyUSB0', 'w')
print('%rrrrrr', file=adausb)


def arrowKeysControl():

        stdscr = curses.initscr()
	curses.cbreak()

	c = 0
        speedA = 0
        speedB = 0

	while True:

	    c = stdscr.getch()                

	    if c == ord('w'):
                speedB = 0
                print('!B00', file=adausb)
                if speedA <= 20:
                    speedA = speedA + 10
                    if speedA > 0:
                        print(('!A' + str(abs(speedA))), file=adausb)
                    elif speedA <
                        print(('!a' + str(abs(speedA))), file=adausb)

	    elif c == ord('a'):
                if speedB <= 10:
                    speedB = speedB + 10
                    if speedB > 0:
                        print(('!B' + str(abs(speedB))), file=adausb)
                    elif speedB < 0:
                        print(('!b' + str(abs(speedB))), file=adausb)
                
	    elif c == ord('d'):
                if speedB >= -10:
                    speedB = speedB - 10
                    if speedB > 0:
                        print(('!B' + str(abs(speedB))), file=adausb)
                    elif speedB < 0:
                        print(('!b' + str(abs(speedB))), file=adausb)

	    elif c == ord('s'):
                speedB = 0
                print('!B00', file=adausb)
                if speedA >= -20:
                    speedA = speedA - 10
                    if speedA > 0:
                        print(('!A' + str(abs(speedA))), file=adausb)
                    elif speedA < 0:
                        print(('!a' + str(abs(speedA))), file=adausb)

            else:
                print('%rrrrrr', file=adausb)
                speedA = 0
                speedB = 0

            if speedA > 0:
                print(('!A' + str(speedA)), file=adausb)

            elif speedA < 0:
                print(('!a' + str(speedA)), file=adausb)

            if speedB > 0:
                print(('!B' + str(speedB)), file=adausb)

            elif speedB < 0:
                print(('!b' + str(speedB)), file=adausb)


arrowKeysControl()
