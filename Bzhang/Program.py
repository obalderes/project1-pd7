from random import randint

def makeGroups(x):

file = open("ml7-student-names", 'r')

period6 = [] #Creates two arrays in order to
period7 = [] #separate the students by periods.

period6Groups = []
period7Groups = []

for line in file
    if line[-1] = 6
        period6.append(line) #Puts all period 6 people into one group
    else
        period7.append(line) #Puts all period 7 people into another

while len(period6) > 0: 
    a = [] #Temporary array a[]
        for i in range(len(period6):
            a.append(period6[i])
                if len(a) == 4:
                    period6Groups.append(a)
                        a = [] 
    
                       #We create sub groups to organize the period even further. Once the temporary array reaches a size of 4, it's added to period6Groups and resets.        
while len(period7) > 0:
    a = [] #Temporary array a[]
        for i in range(len(period7):
                a.append(period7[i])
                    if len(a) == 4:
                        period7Groups.append(a)
                        a = []
                       #Same as period 6       

                       
print period6Groups, period7Groups
                       

    
    
        

      
