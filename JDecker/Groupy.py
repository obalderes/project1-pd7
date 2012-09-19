#James Decker

sox = []
sivin = []

import random
from random import shuffle

for line in open("ml7-student-names").readlines():
	line = line.strip();
	if line.find( "6" ) >= 0:
		sox.append(line)
	else:
		sivin.append(line)

shuffle(sox)
shuffle(sivin)


i = 0
while i < len(sox):
	print sox[i:i+4]
	i = i + 4

j = 0
while j < len(sivin):
	print sivin[j:j+4]
	j = j + 4
