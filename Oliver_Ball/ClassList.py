import random
#random.randint(a,b) returns int a <= int <= b


file = open('ml7-student-names.txt')

nameList = []
period6 = []
period7 = []

for line in file:
    nameList.append(line)

#print nameList

print nameList[0]

