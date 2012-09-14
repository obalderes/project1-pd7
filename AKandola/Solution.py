f = open('ml7-student-names')

lines = ""

for i in f.readlines():
  #print i
  lines += i

#print lines

sixnames = []
sevennames = []

placeholder = ""
name = ""

for i in lines:
  placeholder += i
  #print placeholder
  if (i == '6'):
    sixnames += [placeholder]
    placeholder = ""
  if (i == '7'):
    sevennames += [placeholder]
    placeholder = ""

#print sixnames
#print sevennames

sixlength = len(sixnames)
sevenlength = len(sevennames)

#print sixlength

a = 0
b = 0

#print sixnames
while (a < sixlength):
    sixnames[a] = sixnames[a].replace(",6", "")
    sixnames[a] = sixnames[a].replace('\n', '')
    a += 1

#print sixnames

while (b < sevenlength):
    sevennames[a] = sevennames[a].replace(",7", "")
    sevennames[a] = sevennames[a].replace('\n', '')
    b += 1

import random

sixgroups = []
sevengroups = []


