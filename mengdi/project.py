#!/user/bin/python
import random

f = open("ml7-student-names",'r')
nameList = f.readlines()
nameList.append('None,None,6.')

def ShuffleList(string):
    l=[]
    for index in range(len(nameList)):
        if nameList[index].find(string,0,len(nameList[index]))!=-1:
            l.append(nameList[index])
        random.shuffle(l)
    return l  

def GroupPull(l):
    s=[]
    f=[]
    for index in range(len(l)):
        a=l[index].rfind(',',0,len(l[index]))
        a=l[index].rfind('.',a,len(l[index]))
        l[index] = l[index][:a]
        s.append(l[index])
        if (index+1)%4==0:
            f.append(s)
            s=[]
    return f

def main(string):
    return GroupPull(ShuffleList(string))

for item in main('6'):
    print item
print("\r\n")
for item in main('7'):
    print item



