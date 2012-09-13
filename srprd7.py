
#from random import randrange

names = []
#morenames = {}

for line in open('ml7-student-names').readlines():
    names.append(line.strip())

print names[5:13]
