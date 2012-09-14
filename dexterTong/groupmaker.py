import random

# IT WORKS!

#start of name preparation

file = open( 'ml7-student-names' )
nameList = [line.rstrip('\n') for line in file]
periodSix = []
periodSeven = []
for string in nameList:
    if string.find('6') > -1:
        temp = string[:-2].replace(',',' ')
        last = temp[:temp.find(' ')]
        first = temp[temp.find(' ')+1:]
        name = first+' '+last
        periodSix.append(name)
    else:
        temp = string[:-2].replace(',',' ')
        last = temp[:temp.find(' ')]
        first = temp[temp.find(' ')+1:]
        name = first+' '+last
        periodSeven.append(name)

#end of name preparation)

#start of group assignment

random.shuffle(periodSix)
random.shuffle(periodSeven)
print "\n================PERIOD 6===============\n"
counter=4.0
for name in periodSix:
    if counter % 4 == 0:
        print "Group " + str(int(counter//4))
    print "\t" + name
    counter += 1
print "\n================PERIOD 7===============\n"
counter=4.0
for name in periodSeven:
    if counter % 4 == 0:
        print "Group " + str(int(counter//4))
    print "\t" + name
    counter += 1

#end of program
