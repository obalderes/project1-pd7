import storage

print "Hi"

def getRatings(email):
    return storage.s['id',email]

def rate(email,r1,r2,r3,comment):
    storage.s['responses',email,1] = r1
    storage.s['responses',email,2] = r2
    storage.s['responses',email,3] = r3
    storage.s['responses',email,4] = comment

def getInfo(email):
    namesList =[]
    namesList[1] = storage.s[email,firstName]
    namesList.append(storage.s[email,lastName]
