import shelve

database = shelve.open('database.dat', writeback=True)

def createProj(data):
    """
    creates new entry for Project dictionary given data for that project
    """

projects = {}
projects['1'] = createProj('p1.txt')
database['Projects'] = projects

print database
database.close()
