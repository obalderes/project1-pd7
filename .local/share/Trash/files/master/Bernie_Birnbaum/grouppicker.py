#This is Bernie's group picker project

import random #The random class will be needed to randomize the groups

f = open('ml7-student-names','r') #f is opened here and will be read line-by-line by a separate method
pd6 = [] #Initiallizing this list to be filled with the pd6 people later
pd7 = [] #Initiallizing this list to be filled with the pd7 people later
groups = [] #Initiallizing this list to be filled with the groups later

def main():
    "This function sets the program in motion"
    splitLinesIntoClasses() #This method reads the file line by line, turns each into a 3-element list of the format [last,first,pd\n] and appends this list to the apropriate pd list (ie pd6 or pd7)
    classesToGroups(pd6) #This method takes the pd6 list and divides the elements randomly into lists of four; in the process the pd6 list is emptied
    classesToGroups(pd7) #The same method as above but for pd7
    printGroups() #Once the groups list is populated with 4-element lists of people, this method prints them out nicely

 

def splitLinesIntoClasses():
    "As the title implies, this function reads the file by line, splits each into a list, and add this list to the appropriate class list"
    nameLines = f.readlines()
    for line in nameLines:
        l = line.split(',')
        if '6\n' in l:
            pd6.append(l)
        else:
            pd7.append(l)
    print "end of splitLines"
    
def classesToGroups(l):
    "This function takes a list as a paremeter, randomly creates lists of 4 elements from the list, and adds the new lists to the groups list"
    classList = l
    for i in classList: #The loop runs only as long as classList has elements
        tempGroup = [] #Creating a list for the elements to be stored in until it can be added to the groups list
        for n in range(4): #This loop iterates four times in order to create the groups of 4
            p = random.randrange(0,len(classList)) #p is initiated as a random integer less than the length of classList
            tempGroup.append(classList[p]) #adds the "p-th" element of classList to the current tempGroup
            classList.remove(classList[p]) #removes the "p-th" element from classList to prevent duplicates
        groups.append(tempGroup) #once the tempGroup has four elements, it is appended to the groups list

def lineToString(l):
    "This function takes a list (in the format [last, first, pd#\n]) and returns it as a printable string"
    string = ""
    string = l[1] + " " + l[0] + ", Period " + str(l[2]) #string is now 'First Last, Period pd#\n'; the \n is useful for giving each name a new line when it is printed
    return string

def printGroups():
    "This function prints the groups list in a readable fashion"
    n = 0 #n is used to keep track of which group is being printed
    for i in groups:
        string = "Group " + str(n+1) + ":\n" #string initializes with the group's number
        num = 0 #num is used to call the lineToString function on the "num-th" element of the group
        for l in groups[n]:
            string = string + lineToString(groups[n][num]) #adding each element of the group to string; the new line is a part of each element already
            num = num + 1
        print string #prints one group at a time
        n = n+1

main() #Runs the program
