import shelve
import rating


DIR="OUTPUT"
database = "ratebase"

dbname = "%s/%s"%(DIR,database)

students = open("students.txt","r").readlines()
groups = open("p1.txt").readlines()

A = []
S = []
G = []

def process():
    s = shelve.open(dbname)
    for line in students:
        x = line.split(',')
        email =  str(x[0])
        s[email] = []
    s.close()



def save_rating(email,score):
    s = shelve.open(dbname)
    #group =  util.get_group(email)
    group = "high"
    x = rating.rating("author",score,group)

    if s.has_key(email):
        tmp = s[email]
        tmp.append(x)
        s[email] = tmp
    s.close()

#save_rating("ivansmirnov13@gmail.com",[5,5])

def get_rating(email):
    s=shelve.open(dbname)
    for i in s[email]:
        print i.author
        print i.score
        print i.group
        A.append(i.author)
        S.append(i.score)
        G.append(i.group)
    s.close()

#get_rating("ivansmirnov13@gmail.com")

def authorlist():
    return A

def scorelist():
    return S

def grouplist():
    return G





