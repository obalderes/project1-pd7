# Amanpreet Kandola pd6

# create a string to hold the file
f = open('ml7-student-names')

lines = ""

for i in f.readlines():
  lines += i

# separate the names by period using a placeholder string

sixnames = []
sevennames = []

placeholder = ""

# i is a character. if it is a 6 or a 7, placeholder adds itself into the 
#appropriate list. it then resets itself to nothing
for i in lines:
  placeholder += i
  if (i == '6'):
    sixnames += [placeholder]
    placeholder = ""
  if (i == '7'):
    sevennames += [placeholder]
    placeholder = ""

sixlength = len(sixnames)
sevenlength = len(sevennames)


a = 0
b = 0

#cleaning out the new lists of names to make it easier to read
while (a < sixlength):
    sixnames[a] = sixnames[a].replace(",6", "")
    sixnames[a] = sixnames[a].replace('\n', '')
    a += 1

while (b < sevenlength):
    sevennames[b] = sevennames[b].replace(",7", "")
    sevennames[b] = sevennames[b].replace('\n', '')
    b += 1

#a is now equal to the length of sixnames, and b is equal to the length of sevennames
import random

sixgroups = []
sevengroups = []

group = ""

#take random index of sixnames and add it to group. 
#that index is then removed from the list to avoid repititon
#Do this four times and then
#add group to sixgroups and reset everything. 
while (a > 0):
  total = 0
  while (total < 4):
    number = random.randint(0,a - 1)
    group += sixnames[number]
    sixnames.remove(sixnames[number])
    a -= 1
    total += 1
    group += " "
  sixgroups += [group]
  group = ""

#repeat for sevennames
while (b > 0):
  total = 0
  while (total < 4):
    number = random.randint(0,b - 1)
    group += sevennames[number]
    sevennames.remove(sevennames[number])
    b -= 1
    total += 1
    group += " "
  sevengroups += [group]
  group = ""

#print out the groups in a specific format
grouplength = len(sixgroups)
groupnames = ""
for i in range (0,grouplength):
  groupnames += str(i + 1) + " -  " +sixgroups[i] + "\n"

print groupnames

grouplength = len(sevengroups)
groupnames = ""
for i in range (0,grouplength):
  groupnames += str(i + 1) + "  -  " + sevengroups[i] + "\n"

print groupnames

