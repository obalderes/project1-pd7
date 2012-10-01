import random
import operator
#random.randint(a,b) returns int a <= int <= b

nameList = []
period6 = []
period7 = []

file = open('ml7-student-names.txt')

#copy text file into list
for line in file:
    nameList.append(line)
    


#randomizes list
i = 0
tmp = []
while (nameList.__len__() > 0):
    x = random.randint(0,nameList.__len__() -1 )
    tmp.append( nameList.pop(x) )
    #pop removes and returns an element of a list
    i = i+1
nameList = tmp

#Sorts names into appropriate period and removes the period number from name
for name in nameList:
    if name[-2:-1] == '6':
        period6.append(name[:-3])
    elif name[-2:-1] == '7':
        period7.append(name[:-3])


#Reverse names to First Last
for name in period6:
    tmp = name.split(',')
    name = tmp[1] + ' '  +  tmp[0]
    
for name in period7:
    tmp = name.split(',')
    name = tmp[1] + ' '  +  tmp[0]
    



#Break periods into groups
i = 0
while (i < period6.__len__()):
    period6[i] = str(i/4) + ' ' + period6[i]
    if (operator.mod(i,4) == 3):
        period6[i] = ''.join((period6[i],'\n'))
    i = i+1

i = 0
while (i < period7.__len__()):
    period7[i] = str(i/4) + ' ' + period7[i]
    if (operator.mod(i,4) == 3):
        period7[i] = ''.join((period7[i],'\n'))
    i = i+1

"""
#Print final groups
print 'PERIOD 6 GROUPS:\n'
for name in period6:
    print name   

print '\n\n'

print 'PERIOD 7 GROUPS:\n'
for name in period7:
    print name

"""
