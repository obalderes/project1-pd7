from random import shuffle

##import ml7-student-names line-by-line into lines
lines = [line.strip() for line in open('ml7-student-names')]

##split lines into two separate periods and remove the period numbers
pd6students = []
for pd6student in lines:
    if pd6student[-1] == '6':
        pd6students.append(pd6student[0:-2])
pd7students = []
for pd7student in lines:
    if pd7student[-1] == '7':
        pd7students.append(pd7student[0:-2])

##shuffle the periods
shuffle(pd6students)
shuffle(pd7students)

##split the periods into groups and put everything in a string
counter = 0 

out = "Period 6\n"
while len(pd6students) >0:
    counter += 1
    out += pd6students.pop()
    out += "\t"
    if counter == 3:
        out += "\n"
        counter = 0

out += "Period 7\n\n"
while len(pd7students) > 0:
    counter += 1
    out += pd7students.pop()
    out += "\t"
    if counter == 3:
        out += "\n"
        counter = 0

##output the string into a tsv file
#text_file = open("groups.csv", "w")
#text_file.write(out)
#text_file.close()

#print out the string
print out