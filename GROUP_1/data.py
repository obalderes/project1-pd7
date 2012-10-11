#this is what creates the personal info and group databases/shelves
#Ratings are lists of strings in the format [email,q1,q2,q3,q4,comment]
#A blank rating should have 0's for question answers and empty string for the comment
#the key for the ratings shelve is the rater's email, the data at it is a list of lists
#feel free to add more functions if you need, or ask me to

import shelve

Pd6 = shelve.open('databases/GroupInfoPd6.dat')
Pd7 = shelve.open('databases/GroupInfoPd7.dat')
info = shelve.open('databases/PersonalInfo.dat')
ratings = shelve.open('databases/ratings.dat')
questions = []

class data:

#WORKS
    @staticmethod
    def __init__():
        if not ('databases/GroupInfoPd6.dat' and 'databases/GroupInfoPd7.dat' and 'databases/PersonalInfo.dat' and 'databases/ratings.dat'):
            makeShelves()

#WORKS
    @staticmethod
    def makeShelves():
        students = open('databases/students.txt')
        sList = students.readlines()
        students.close() 
        i = 0
        while i<8:
            Pd6[str(i)]=list()
            Pd7[str(i)]=list()
            i+=1
        for line in sList:
            email = line[ : line.find(',')].lower()
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
        questionText = open('databases/questions.txt')
        q = questionText.readlines()
        questionText.close()
        for line in q:
            questions.append(line)
        for group in Pd6:
            temp=Pd6[group]
            ratings[temp[0]] = [[temp[1],'0','0','0','0',''], [temp[2],'0','0','0','0',''], [temp[3],'0','0','0','0',''] ]
            ratings[temp[1]] = [[temp[0],'0','0','0','0',''], [temp[2],'0','0','0','0',''], [temp[3],'0','0','0','0',''] ]
            ratings[temp[2]] = [[temp[0],'0','0','0','0',''], [temp[1],'0','0','0','0',''], [temp[3],'0','0','0','0',''] ]
            ratings[temp[3]] = [[temp[0],'0','0','0','0',''], [temp[1],'0','0','0','0',''], [temp[2],'0','0','0','0',''] ]
        for group in Pd7:
            temp=Pd7[group]
            ratings[temp[0]] = [[temp[1],'0','0','0','0',''], [temp[2],'0','0','0','0',''], [temp[3],'0','0','0','0',''] ]
            ratings[temp[1]] = [[temp[0],'0','0','0','0',''], [temp[2],'0','0','0','0',''], [temp[3],'0','0','0','0',''] ]
            ratings[temp[2]] = [[temp[0],'0','0','0','0',''], [temp[1],'0','0','0','0',''], [temp[3],'0','0','0','0',''] ]
            ratings[temp[3]] = [[temp[0],'0','0','0','0',''], [temp[1],'0','0','0','0',''], [temp[2],'0','0','0','0',''] ]

#given email and ID, returns true if login is valid, false otherwise. THIS WORKS
    @staticmethod
    def checkLogin(username, password):
        try:
            temp=info[username.lower()]
            if temp[2] == password:
                return True
            return False
        except:
            return False

#gets the person given an email
    @staticmethod
    def getName(username):
        temp=info[username.lower()]
        return temp[1] + ' ' + temp[0]

#gets the group a person belongs to given their email
    @staticmethod
    def getGroupNo(username):
        temp=info[username.lower()]
        return temp[4]

#gets the period a person is in (0 for 1 and 1 for 7) given their email
    @staticmethod
    def getPeriod(username):
        temp=info[username.lower()]
        return temp[3]

#returns the emails of the group members given the group number and period, in a list
    @staticmethod
    def getGroup(num, period):
        if period == 0:
            return Pd6[num]
        return Pd7[num]

    @staticmethod
    def getGroup(username):
        temp=info[username.lower()]
        period=temp[3]
        group = temp[4]
        if period == 0:
            return Pd6[group]
        else:
            return Pd7[group]

#given an email, returns the ratings of the person as a list of lists. this took a lot of thought to write
    @staticmethod
    def getRatingsOf(username):
        temp=info[username.lower()]
        ratelist=[]
        period=temp[3]
        group=temp[4]
        if period == 0:
            temp2 = Pd6[group]
        else:
            temp2 = Pd7[group]
        for email in temp2:
            if not email == username.lower():
                temp3 = ratings[email]
                for entry in temp3:
                    if entry[0] == username.lower():
                        ratelist.append(entry)
        return ratelist

#given an email, returns ratings made by this person
    @staticmethod
    def getMyRatings(username):
        return ratings[username.lower()]
            

#creates/modifies a rating given the email of the rater, email of the ratee, their question answers, and comments
    @staticmethod
    def setRating(rater, ratee, q1, q2, q3, q4, comment):
        
