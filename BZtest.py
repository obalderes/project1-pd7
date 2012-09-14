L = []
names6 = []
names7 = []

def reader(data):
    """
    reads the file into a list
    """
    return open(data).readlines()

L = reader("ml7-student-names")
n = len(L)

#for item in L:
#    item = item.strip()
#    print item

for item in L:
    item = item.strip()
    if (item[-1] == "7"):
        names7.append(item)
    else:
        names6.append(item)

print "Period 6"
for item in names6:
    print item

print

print "Period 7"
for item in names7:
    print item



