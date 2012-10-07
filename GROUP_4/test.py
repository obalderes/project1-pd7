import shelve
import database


#auth = shelve.open("authen")
#print auth["fallenpwr@gmail.com"]

groups = shelve.open("groups")
print groups["fallenpwr@gmail.com"]
