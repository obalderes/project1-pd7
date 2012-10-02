import shelve
emails = shelve.open("emails") #key: str(num 0-15) info: emails in lists

def prepro_p1():
    f=open("p1.txt",'r')
    nameList=[]
    emailList=[]
    key=""
    comma=0
    comma2=0
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



      
