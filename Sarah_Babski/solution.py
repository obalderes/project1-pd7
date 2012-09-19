#!/user/bin/python
import random

#group by period
six=[]
seven=[]
for name in open("ml7-student-names", "r").readlines():
    name.strip()
    name.split(",")
    fname = name[0]+", "+name[1]
    if name[2] == "6":
        six.append(fname)
    else:
        seven.append(fname)

#randomize
def randomize(period,list):
    random.shuffle(list)
    groupnum=1;n=1
    for name in list:
        if n<=4:
            print period+"."+groupnum+" "+fname+"\n"
            n=n+1
        else:
            groupnum=groupnum+1
            print period+"."+groupnum+" "+fname+"\n"
            n=2
            
randomize(6,six)
randomize(7,seven)
