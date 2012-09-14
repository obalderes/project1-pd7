f = open("names", "r");
lines = f.readlines();
print lines;

pd6 = [];
pd7 = [];

for line in lines:
    line = line.strip();
    if line[-1] == 6:
        pd6.append(line);
    elif line[-1] == 7:
        pd7.append(line);

print lines;
print pd6
print pd7
