from random import shuffle
lines = [line.strip() for line in open('ml7-student-names')]
pd6students = []
for pd6student in lines:
    if pd6student[-1] == '6':
        pd6students.append(pd6student[0:-2])
pd7students = []
for pd7student in lines:
    if pd7student[-1] == '7':
        pd7students.append(pd7student[0:-2])
shuffle(pd6students)
shuffle(pd7students)
counter = 1
out = "Period 6\n"
while len(pd6students) >0:
    counter += 1
    out += pd6students.pop()
    out += "\t"
    if counter == 4:
        out += "\n"
        counter = 1
out += "Period 7\n"
while len(pd7students) > 0:
    counter += 1
    out += pd7students.pop()
    out += "\t"
    if counter == 4:
        out += "\n"
        counter = 1
text_file = open("groups.tsv", "w")
text_file.write(out)
text_file.close()
