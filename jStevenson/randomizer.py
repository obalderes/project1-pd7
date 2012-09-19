import random
def randomize(file, period, group_size):
    """randomize takes three variables: file (str), period (int) and group_size (int)"""
    lineList = (open(file, "r").readlines())
    random.shuffle(lineList)
    realList = []
    for line in lineList:
        line = line.strip().split(",")
        line[-1] = int(line[-1])
        if line[-1] == period:
            realList.append(line)
    for i in range(len(realList)):
        realList[i] = realList[i][1] + " " + realList[i][0]
    groupNum = len(realList) // group_size + 1
    groupList = []
    for i in range(groupNum):
        groupList += [realList[group_size*i:group_size*(i+1)]]
    for group in groupList:
        for name in group:
            print(name)
        print("\n")
