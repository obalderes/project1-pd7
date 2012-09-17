import random

file = open("ml7-student-names")
tmpinfo = ""
initiallist = []
for line in file:
	tmpinfo = line
	tmpinfo = tmpinfo.strip()
	initiallist.append(tmpinfo)

randomizedlist = []
numnames = len(initiallist)
while len(randomizedlist) < numnames:
	r = random.randint(0,len(initiallist)-1)
	randomizedlist.append(initiallist[r])
	initiallist.pop(r)	
	
pdsix = []
pdseven = []
for name in randomizedlist:
	if name.find('6') >= 0:
		pdsix.append(name)
	else:
		pdseven.append(name)

print 'Period 6'
teamnumber = 0
for name in pdsix:
	firstname = name.split(',')[1]
	if teamnumber%4 == 0:
		print '\n'
		print 'Team:',(teamnumber/4)+1
	print firstname
	teamnumber=teamnumber+1

print '\n','Period 7'
teamnumber = 0
for name in pdseven:
	firstname = name.split(',')[1]
	if teamnumber%4 == 0:
		print '\n'
		print 'Team:',(teamnumber/4)+1
	print firstname
	teamnumber=teamnumber+1
	
	
