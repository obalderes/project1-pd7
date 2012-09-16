import random

per6_info = []
per7_info = []

for line in open("ml7-student-names", "r").readlines():
    if (line.find("6") != -1):
        per6_info.append(line.strip())
    else:
        per7_info.append(line.strip())

random.shuffle(per6_info)
random.shuffle(per7_info)

for i in range(len(per6_info)):
    if i%4 == 0:
        print "\n 6"
    print per6_info[i] + "\n"

for i in range(len(per7_info)):
    if i%4 == 0:
        print "\n 7"
    print per7_info[i] + "\n"
