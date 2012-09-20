# Adam Schorin
# Period 6

#script. to hell with functions

import random

#lists for each class
names6 = []	
names7 = []

#divides list into two classes
for line in open("ml7-student-names.txt").readlines():
	line = line.strip()
	if line.find("6") != -1:
		names6.append(line)
	if line.find("7") != -1:
		names7.append(line)

		
random.shuffle(names6)
random.shuffle(names7)
n = 0
for name in names6:
	print name
	n += 1
	if 	n == 4:
		print "\n"
		n = 0
print "\n \n"
n = 0
for name in names7:
	print name
	n+=1 
	if n == 4:
		print "\n"
		n = 0


