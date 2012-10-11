#i've been using this to test data.py code
#this is nonessential to the feedbackerator

from data import *

d = data()
d.makeShelves()
print d.checkLogin('SCHOOLPURPOSES@gmail.com','8758')
print d.getName('Chabma@gmail.com')
print d.getGroupNo('ScHOolPuRpOSES@gmaiL.cOm')
print d.getPeriod('wu.allEn154@gmail.com')
print d.getGroup('obalderes@gmail.COM')
d.setRating('CHaBmA@gmail.com','schoolPurPoses@gmaiL.com', '1', '9', '3', '5', "Dexter was an awesome coder")
print d.getMyRatings('chabma@gmail.com')
print d.getRatingsOf('schOOlpurposes@gmail.com')
