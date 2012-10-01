l=[]
f = open("ml7-student-names", 'r')

for line in f:
	line = line.strip() #removes '\n' from the lines in the files
	l.append(line) #adds each line to list 'l'

six = [] 
seven = []

for string in l:
	if '6' in string:
		six.append(string) #adds names to 6th period class
	else:
		seven.append(string) #adds names to 7th period class

import random

random.shuffle(six) #randomizes the order of the strings in the list
random.shuffle(seven)

def printG(L, n):
	"""
	printG takes list, L, and separates the names into groups of n.
	It prints each string in list L line by line. After n names, it prints an empty line to differentiate between the groups. 
	Example: 
	printG(L,2) >>
		A,B,6
		C,D,6
		
		E,F,6
		G,H,6 (and so on...)
	"""
	for string in L:
		print string
		if ((L.index(string)+1) % n) ==0:
			print "\n"
	
print "***6th Period***"
printG(six, 4)

print "\n***7th Period***\n"
printG(seven, 4)
