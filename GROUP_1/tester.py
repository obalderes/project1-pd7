#i've been using this to test data.py code

from data import *

d = data()
d.makeShelves()
print d.checkLogin('schoolpurposes@gmail.com','8758')
print d.getName('Chabma@gmail.com')
print d.getGroupNo('ScHOolPuRpOSES@gmaiL.cOm')
print d.getPeriod('wu.allen154@gmail.com')
print d.getGroup('obalderes@gmail.com')
print d.getMyRatings('schoolpurposes@gmail.com')
print '\n\n'
print d.getRatingsOf('schoolpurposes@gmail.com')
