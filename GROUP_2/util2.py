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



def save_rating(email,author,score,group):
    s = shelve.open(dbname)
    x = rating.rating(author,score,group)

    if s.has_key(email):
        tmp = s[email]
        tmp.append(x)
        s[email] = tmp
    else:
        print "not saved"
    
    s.close()

#save_rating("ivansmirnov13@gmail.com",[5,5])

def get_rating(email):
    A = []
    S = []
    G = []
    s=shelve.open(dbname)
    if s.has_key(email):
        for i in s[email]:
            A.append(i.author)
            S.append(i.score)
            G.append(i.group)
    s.close()
    return A,S


#get_rating("ivansmirnov13@gmail.com")

def authorlist():
    return A

def scorelist():
    return S

def grouplist():
    return G





