import random

def readFileIntoArrayByLine(filename):
    file = open(filename, "r")
    lines = [line.rstrip() for line in file]
    file.close()
    return lines

def createPeriodStudentsDict(lines):
    studentsByPeriod = {}
    for line in lines:
        period = line[-1] #period is assured to be the last character
        name = line[:-2] #name is assured to be everything but the last 2 characters
        if period not in studentsByPeriod:
            studentsByPeriod[period] = []
        studentsByPeriod[period].append(name)    
    return studentsByPeriod

def printGroups(studentsByPeriod):
    #printed format is period-group-name
    #periods are sorted first
    periods = studentsByPeriod.keys()
    periods.sort()
    for period in periods:
        students = studentsByPeriod[period]
        currentGroup = 0
        for i in range(len(students)):
            if i % 4 == 0:
                #updates intitally and then after every 4 iterations
                currentGroup += 1
            print("%s-%s-%s" % (period, currentGroup, students[i]))

if __name__ == "__main__":
    filename = "ml7-student-names"
    lines = readFileIntoArrayByLine(filename)
    #Array of lines are shuffled so that they're already in a random order when
    #read into a more appropriate data structure
    random.shuffle(lines)
    studentsByPeriod = createPeriodStudentsDict(lines)
    printGroups(studentsByPeriod)
