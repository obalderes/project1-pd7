import random #To sort the students randomly, we will need to use random

print "START!" #Because we're going to start...now.

hihi = open('ml7-student-names', 'r').readlines() #Creates a list where each element is a line from "ml7-student-names". Every element has the name and period of a student.


#Creates 2 lists, one which has all the students in period 6, and one which has all the students in period 7.
six = []
for x in hihi:
    if x.find('6') >0:
        six.append(x)

seven = []
for x in hihi:
    if x.find('7') >0:
        seven.append(x)

#Randomizes the list orders
random.shuffle(six)
random.shuffle(seven)

# g will be used for group numbers; i will be used to create an empty line every 4 students, signifying a group.
g = 1
i = 0

#prints out groups for period 6
for x in six:
    if (i % 4 == 0):
        print ""
        print "Group " + str(g) +":"
        g = g + 1
    z = x.find(',6')
    print x[0:z]
    i = i + 1

# g is reset for the period 7 groups, j is used instead of i to make it 20% cooler.
g = 1
j = 0

#prints out groups for period 7
for x in seven:
    if (j % 4 == 0):
        print ""
        print "Period 7 Group " + str(g) +":"
        g = g + 1
    z = x.find(',7')
    print x[0:z]
    j = j + 1

#prints out sizes of each class as an added bonus
print ""
print "Size of classes: " + str(i) + ", " + str(j)
