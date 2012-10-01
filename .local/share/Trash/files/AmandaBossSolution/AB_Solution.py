#Amanda Boss
#!/user/bin/python
import random

period6 = list()
period7 = list()

for lines in open("ml7-student-names", "r").readlines():
    lines1 = lines.strip()
    #lines2 = lines1.split(",")
    lines2 = lines1.strip("/n") 
    if (lines2.find('7') == -1):
       period6.append(lines2)
    if (lines2.find('6') == -1):
       period7.append(lines2)

def shufflePeriod6():
    for people in period6:
        print people
        if(period6.index(people)) % 4 == 2: #The empty line is added
           print "\n  Next Group:"          #after every four lines
                                            #so a group can be made
            
def shufflePeriod7():
    for people in period7:
        print people
        if(period7.index(people)) %4 == 2:
            print "\n  Next Group:" 
            

def RandomizeList(Period):
    random.shuffle(Period) #so the list is actually random, not in ABC order
    if Period == period6:
        shufflePeriod6()
    if Period == period7:
        shufflePeriod7()

# Note: this procedure leaves one person without a group in Period 7 and goes in
#first name, last name, period form
print "6th Period Groups:"
RandomizeList(period6)

print "\n7th Period Groups:\n"
RandomizeList(period7)
