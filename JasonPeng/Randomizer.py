from random import choice

six = []
seven = []
names = []

for line in open("ml7-student-names", "r").readlines():
    a = line.strip()
    names.append(a)

for person in names:
    if "6" in person:
        six.append(person)
    else:
        seven.append(person)

print "Period 6:"
sizesix = len(six)
count = 0
while(len(six) > 0):
    if count == 4:
        print "\n "
        count = 0
    else:
        x = choice(six)
        print x
        six.remove(x)
        count = count + 1

print "\nPeriod 7:"

count2 = 0
while(len(seven) > 0):
    if count2 == 4:
        print "\n "
        count2 = 0
    else:
        x = choice(seven)
        print x
        seven.remove(x)
        count2 = count2 + 1






    






    

