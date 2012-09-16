def Randomizer():
    f = open('m17-student-names')
    f.readlines
    import random
    #Setup^
    x = 0
    y = 0
    r[0] = 0
    while (x < len(f)):
    	y = random.randint(0, len(f))
    	if not r[y]:
    		f[x] = r[y]
    		x = x+1
    #Randomized^
    f.split(',')
    x = 0
    y = 0
    z = 0
    G6[0]= 0
    G7[0]= 0
    while (x < len(r)):
    	if f[3 * x] == '6':
    		G6[y] = r[x]
    		y = y+1
    	else :
    		G7[z] = r[x]
    		z = z + 1
    #Seperated^
    x =0
    Groups6[0] = 0
    Groups7[0] = 0
    while ((x * 4) < len(G6)):
        Groups6[x] = G6[x]+" "+G6[x+1]+" "+G6[x+2]+" "+G6[x+3]
        x = x + 1
    x =0
    while ((x * 4) < len(G7)):
        Groups7[x] = G7[x]+" "+G7[x+1]+" "+G7[x+2]+" "+G7[x+3]
        x = x + 1
    Result[0]= Groups6
    Result[1]= Groups7
    return Result
