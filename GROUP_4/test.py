import shelve

auth = shelve.open("authen")
print auth["fallenpwr@gmail.com"]
