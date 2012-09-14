def randomize(group_size, file):
    lineList = open(file, "r").readlines().shuffle()
    for line in lineList:
        line = line.split( ,)
