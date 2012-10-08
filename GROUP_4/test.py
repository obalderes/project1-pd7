import shelve
import database


auth = shelve.open("authen")
print auth["jpengsmail@gmail.com"]

#groups = shelve.open("groups")
#print groups["fallenpwr@gmail.com"]

#print database.getRatings("jpengsmail@gmail.com")
"""
f =  open("questions.txt", "r").readlines()

print f[0].strip()
print f[0]
"""
