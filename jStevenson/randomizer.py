import re, random
def randomize(group_size, file):
    lineList = random.shuffle(open(file, "r").readlines())
    for line in lineList:
        line = re.split(" |,", line)
    print(line)
    groupNum = list.length // group_size + 1
    groupList = []
    for i in range(groupNum):
        groupList += lineList[4*i:4*(i+1)]
    print(groupList)
