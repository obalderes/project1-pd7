period6 = list()
period7 = list()

for text in open("ml7-student-names","r").readlines():
    firstname = " "
    lastname = " "
    text=text.strip()
    lastname = text[:text.index(",")]
    firstname = text[text.index(",")+1:text.rindex(",")]
    if text[text.rindex(",")+1:] == "6":
        period6.append(firstname + " " + lastname)
    else:
        period7.append(firstname + " " + lastname)
print period6[80]
print period6
print period7
