#!/usr/bin/python
import fileinput
import random

def solution():
	names = open("ml7-student-names", "r")
	names6 = []
	names7 = []
	for line in names.readlines():
		period = (line.split(","))[2]
		if "6" in period:
			names6.insert(random.randrange(0, len(names6) + 1),(line.split(","))[1] + " " + (line.split(","))[0])
		else:
			names7.insert(random.randrange(0, len(names7) + 1),(line.split(","))[1] + " " + ((line.split(","))[0]))
	names.close()
	x = 4
	while x < len(names6):
		names6.insert(x, "")
		x += 5
	x = 4
	while x < len(names7):
		names7.insert(x, "")
		x += 5
	print "Period 6 groups: \n"
	for name in names6:
		print name + "\n"
	print "\nPeriod 7 groups: \n"
	for name in names7:
		print name + "\n"

solution()
