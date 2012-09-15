from random import shuffle

pd6 = []
pd7 = []

for line in open("ml7-student-names").readlines():
    line = line.strip()
    a,b,c = line.split(",")
    if c is '6':      # c is the period number (a is first name, b is last name)
        pd6.append(b+a+c) #if needbe, can manually reinsert ',' in order to help remake the original form of the data at the end
    else:
        pd7.append(b+a+c)


#print pd6              ## Commented out parts were
shuffle(pd6)            ## used to make sure that
#print ""               ## shuffle actually shuffled
#print pd6

#print pd7
shuffle(pd7)
#print ""
#print pd7

counter = 0
for name in pd6:
    if counter <= 3:
        print name                 # makes groups of 4 for pd6
        counter+= 1
    else:
        print 
        print name
        counter = 1

print                  ## just created a line of separation between periods

counter = 0
for name in pd7:
    if counter <= 3:
        print name                 # makes groups of 4 for pd7
        counter+= 1
    else:
        print
        print name
        counter = 1
