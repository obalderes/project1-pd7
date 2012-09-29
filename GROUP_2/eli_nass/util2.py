import shelve
import rating


DIR="OUTPUT"
database = "ratebase"

dbname = "%s/%s"%(DIR,database)

students = open("students.txt","r").readlines()
groups = open("p1.txt").readlines()


def process():
    s = shelve.open(dbname)
    for line in students:
        x = line.split(',')
        email =  str(x[0])
        s[email] = []
    s.close()

def save_rating(email):
    group = 100
    for line in groups:
        x = line.split(',')
        
        if email in x[1:]:
            group = x[0]
            

    s = shelve.open(dbname)

    x = rating.rating("author",[5,4,3,2,1],group)
    if s.has_key(email):
        tmp = s[email]
        tmp.append(x)
        s[email] = tmp
    s.close()

def get_rating(email):
    s=shelve.open(dbname)
    for i in s[email]:
        print i.author
        print i.score
        print i.group
    s.close()

