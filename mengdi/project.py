import random

def creatList():
    x = [[i] for i in range(63)]
    random. shuffle(x)
    return x

f = open("ml7-student-names",'r')
nameList = f.readlines()
print nameList[1];


def Period6():
    Period6=[]
    for index in range(len(nameList)):
        if nameList[index].find('6',0,len(nameList[index]))!=-1:
            Period6.append(nameList[index])
    return Period6
print Period6()
            


 
 



