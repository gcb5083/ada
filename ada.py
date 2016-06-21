#!/usr/bin/env python

from __future__ import print_function
import os.path
import curses
import time

controls = '\t1: Arrow Keys\t2: Trackpad\t3: Mouse\t'

adausb = open('/dev/ttyUSB0', 'w')
print('%rrrrrr', file=adausb)


def openUSBPort():
	usbport = 0

	for ii in range(4, 0):
		if os.path.isfile('dev/ttyUSB' + str(ii)):
			usbport = ii
			break

	adausb = open('/dev/ttyUSB' + str(usbport))

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

def arrowKeysControl():
	stdscr = curses.initscr()
	curses.cbreak()
	c = 0
	while c != 8:
	    c = stdscr.getch()
	    if c == ord('w'):
		print('!A40', file=adausb)
	    	time.sleep(1)
	    elif c == ord('s'):
		print('!a40', file=adausb)
	    	time.sleep(1)
	    elif c == ord('a'):
		print('!B40', file=adausb)
	    	time.sleep(1)
	    elif c == ord('d'):
		print('!b40', file=adausb)
	    	time.sleep(1)

	    print('%rrrrrr', file=adausb)

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
