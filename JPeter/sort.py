file = open("ml7-student-names","r")
string = file.read()

a = string.split('\n')
b = []
period6 = []
period7 = []

for x in a: 
    x = x.split(',')
    b.append(x);

for student in b:
    for data in student:
        print data
        if data == '6':
            period6.append(student)
        if data == '7':
            period7.append(student)
            
print 'STUDENTS IN PERIOD 6'
for student in period6:
    print student[1] + ' ' + student[0]
 
print '\nSTUDENTS IN PERIOD 7'       
for student in period7:
    print student[1] + ' ' +  student[0]





