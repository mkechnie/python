#!/usr/bin/python

import sys, tty, termios

possibilities = []
descriptors = []
f = open(sys.argv[1], 'r')
for line in f:
	possibleAction=line.split('|')
	if len(possibleAction) == 1:
		possibilities.append(possibleAction[0])
		descriptors.append(possibleAction[0])
	else:
		possibilites.append(possibleAction[0] + '\n')
		descriptors.append(possibleAction[1])

sys.stderr.write("\n")
index = 0
for desc in descriptors:
	if index > 9:
		line = chr(index + 87) + ":	" + desc
	else:
		line = str(index) + ":	" + desc
	sys.stderr.write(line)
	index = index + 1

fd = sys.stdin.fileno()
old_settings= termios.tcgetattr(fd)
tty.setraw(sys.stdin.fileno())
ch = sys.stdin.read(1)
termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

if ch != "Q":
	index = 0
	asc = ord(ch)
	if asc > 96:
		index = asc - 87
	else:
		index = int(ch)
	print possibilities[index],

sys.stderr.write("\n")


