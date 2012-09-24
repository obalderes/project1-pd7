import random

#import names into a list
names=[]
for line in open('ml7-student-names'):
    names.append(line.strip())

#split names in respective periods and remove the period
pd6 = []
for student in names:
    if student[-1] == '6':
        pd6.append(student[0:-2])
pd7 = []
for student in names:
    if student[-1] == '7':
        pd7.append(student[0:-2])

#shuffle names
random.shuffle(pd6)
random.shuffle(pd7)

#split names into groups of 4
count = 0
output = 'PD6'+'\n'
while len(pd6) > 0:
    output += pd6.pop() + '\t'
    count += 1
    if count == 4:
        count = 0
        output += '\n'
output += '\n\n' + 'PD7' + '\n'
count = 0
while len(pd7) > 0:
    output += pd7.pop()
    output += '\t'
    count += 1
    if count == 4:
        count = 0
        output += '\n'

#print out result
print output


