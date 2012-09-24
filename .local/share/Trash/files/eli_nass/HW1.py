from random import shuffle

period6 = []
period7 = []

for line in open("names.txt").readlines():
    #Strip will remove extra white spaces
    line = line.strip()
    last,first,period = line.split(',')

    #Organize by period
    if period is '6':
        period6.append(first+' '+ last)
    if period is '7':
        period7.append(first+' '+ last)

#Shuffle both periods
shuffle(period6)
shuffle(period7)

def Grouper(period):
    count = 0
    group = 1
    for i in period:

        if count == 0:
            print "\n"           
            #reset count every 4 people
            print "GROUP "+ str(group)
            group = group + 1
            #increase group display
        print i
        count = count + 1
        if count is 4:
            count = 0
print "PERIOD 6"    
Grouper(period6)

print "PERIOD 7"
Grouper(period7)
