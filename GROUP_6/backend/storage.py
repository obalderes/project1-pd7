import shelve
s = shelve.open('info.dat')
s['id'] = []
s['responses'] = []
temp = s['id']
for x in range(0,10):
    temp.append('john@doe.com')
s['id'] = temp
print s