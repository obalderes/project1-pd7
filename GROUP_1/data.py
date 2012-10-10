
#this is what creates the personal info and group databases/shelves

import shelve

Pd6 = shelve.open('databases/GroupInfoPd6.dat')
Pd7 = shelve.open('databases/GroupInfoPd7.dat')
info = shelve.open('databases/PersonalInfo.dat')
ratings = shelve.open('databases/ratings.dat')

class data:

    def __init__():
        makeInfoGroups()

    def makeInfoGroups():
        students = open('databases/students.txt')
        sList = students.readlines()
        students.close() 
        i = 0
        while i<8:
            Pd6[str(i)]=list()
            Pd7[str(i)]=list()
            i+=1
            for line in sList:
                email = line[ : line.find(',')]
                line = line[line.find(',',1) : ]
                last = line[1 : line.find(',',1)]
                line = line[line.find(',',1) : ]
                first = line[1 : line.find(',',1)]
                line = line[line.find(',',1) : ]
                ID = line[1 : line.find(',',1)]
                line = line[line.find(',',7) : ]
                period = line[1:line.find(',',1)]
                group=line[-2]
                info[email] = [ last, first, ID, period, group]
                if period>'0':
                    temp=Pd7[group]
                    temp.append(email)
                    Pd7[group]=temp
                else:
                    temp=Pd6[group]
                    temp.append(email)
                    Pd6[group]=temp
    #insert rating DB making code here
            for group in Pd6:
                temp=Pd6[group]
                ratings[temp[0]] = [ temp[1], temp[2], temp[3] ]
                ratings[temp[1]] = [ temp[0], temp[2], temp[3] ]
                ratings[temp[2]] = [ temp[0], temp[1], temp[3] ]
                ratings[temp[3]] = [ temp[0], temp[1], temp[2] ]
            for group in Pd7:
                temp=Pd7[group]
                ratings[temp[0]] = [ temp[1], temp[2], temp[3] ]
                ratings[temp[1]] = [ temp[0], temp[2], temp[3] ]
                ratings[temp[2]] = [ temp[0], temp[1], temp[3] ]
                ratings[temp[3]] = [ temp[0], temp[1], temp[2] ]


#given email and ID, returns true if login is valid, false otherwise
    def checkLogin(username, password):
        try:
            temp=info[username]
            if temp[2] == password:
                return true
            return false
        except:
            return false

#gets the person given an email, if invalid returns an empty string
    def getName(username):
        try:
            temp=info[username]
            return temp[0] + ' ' + temp[1]
        except:
            return ""

#gets the group a person belongs to given their email, if invalid returns -1
    def getGroupNo(username):
        try:
            temp=info[username]
            return temp[4]
        except:
            return -1

#gets the period a person is in (0 for 1 and 1 for 7) given their email, if invalid returns -1
    def getPeriod(username):
        try:
            temp=info[username]
            return temp[3]
        except:
            return -1

#returns the emails of the group members given the group number and period, in a list, if invalid, returns an empty list.
    def getGroup(num, period):
        try:
            if period == 0:
                return Pd6[num]
            else:
                return Pd7[num]
        except:
            return []

#given an email, returns the ratings of the person as a list of lists
    def getRatingsOf(username):
        pass

#given an email, returns ratings made by this person
    def getMyRatings(username):
        pass

#creates/modifies a rating given the email of the rater, email of the ratee, their question answers, and comments
    def setRating(rater, ratee, q1, q2, q3, q4, comment):
        pass