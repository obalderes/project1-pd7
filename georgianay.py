l=[]
f = open("ml7-student-names", 'r')
for line in f:
	line = line.strip()
	#print(line)
	l.append(line)
#print(l)
six = []
seven = []
for string in l:
	if '6' in string:
		six.append(string)
	else:
		seven.append(string)
#print(six)
#print(len(six))
#print(seven)
#print(len(seven))

