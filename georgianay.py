l=[]
f = open("ml7-student-names", 'r')

for line in f:
	line = line.strip() #removes '/n' from the lines in the files
	l.append(line) #adds each line to list 'l'

six = [] 
seven = []

for string in l:
	if '6' in string:
		six.append(string) #adds names to 6th period class
	else:
		seven.append(string) #adds names to 7th period class

import random

def randomizeL(L):
	random.shuffle(L) #shuffles the items in the list randomly

randomizeL(six)
randomizeL(seven)


# TODO: print four names together; then a space