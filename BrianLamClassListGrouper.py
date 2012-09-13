#Create lists for period 6 and 7
list6 = list()
list7 = list()

for text in open("ml7-student-names", "r").readlines():
    text = text.strip()
    last,first,period = text.split(",")
    if (period == "6"):
        list6.append(first+ " " + last)
    else:
        list7.append(first+ " "+ last)

print "Period 6"
for element in list6:
    print element

print " "

print "Period 7"
for element in list7:
    print element
