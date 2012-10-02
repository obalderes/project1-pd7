import shelve
emails = shelve.open("emails") #key: str(num 0-15) info: emails in lists
students = shelve.open("students") #key: str(emails) info: student info in dictionaries

def prepro_p1():
    f=open("p1.txt",'r')
    emailList=[]
    key=""
    for line in f.readlines():
        line= line.strip()
        if line in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']:
            if key!="":
                emails[key]=emailList
                emailList=[]
                if len(line)>1 and line[1]!=" ":
                    key=line[0:2]
                else:
                    key=line[0]
            elif line!=" ":
                emailList.append(line)
prepro_p1()
print emails

def prepro_students():
    s=open("students.txt",'r')
    key =""
    for line in s.readlines():
        line = line.strip()
        e = line.partition(',')
        info = e[2].split(',')
        students[e[0]]={"Last":info[0],"First":info[1],"ID":info[2],"Class":info[3],"Section":info[4],"Period":info[5],"Group":info[6]}
        
prepro_students()
#print students
      
