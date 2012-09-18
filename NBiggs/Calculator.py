from Tkinter import *

window = Tk()
b1 = Button(window,text='1')
b2 = Button(window,text='2')
b3 = Button(window,text='3')
b4 = Button(window,text='4')
b5 = Button(window,text='5')
b6 = Button(window,text='6')
b7 = Button(window,text='7')
b8 = Button(window,text='8')
b9 = Button(window,text='9')
b10 = Button(window,text='0')
b11 = Button(window,text='.')
b12 = Button(window,text='=')
b13 = Button(window,text='+')
b14 = Button(window,text='-')
b15 = Button(window,text='*')
b16 = Button(window,text='/')
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b10.grid(row=4,column=1)
b11.grid(row=4,column=0)
b12.grid(row=4,column=2)
b13.grid(row=1,column=3)
b14.grid(row=2,column=3)
b15.grid(row=3,column=3)
b16.grid(row=4,column=3)
buttons = [b1,b2,b3,b4,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16]

ans = 0
showing = 0
curfunc = ''

def but1():
	global showing
	global ans
	if ans == 0:
		showing = 1
		ans = 1
	else:
		if showing > 0:
			showing = (showing*10) + 1
		else:
			showing = 1
	display = Label(window,text=showing)
	display.grid(row=0,column = 3)
def but2():
	global showing
	global ans
	if ans == 0:
		showing = 2
		ans = 2
	else:
		if showing > 0:
			showing = (showing*10) + 2
		else:
			showing = 2
	display = Label(window,text=showing)
	display.grid(row=0,column = 3)
def but2():
	global showing
	global ans
	if ans == 0:
		showing = 2
		ans = 2
	else:
		if showing > 0:
			showing = (showing*10) + 2
		else:
			showing = 2
	display = Label(window,text=showing)
	display.grid(row=0,column = 3)
def but3():
	global showing
	global ans
	if ans == 0:
		showing = 3
		ans = 3
	else:
		if showing > 0:
			showing = (showing*10) + 3
		else:
			showing = 3
	display = Label(window,text=showing)
	display.grid(row=0,column = 3)
def but4():
	global showing
	global ans
	if ans == 0:
		showing = 4
		ans = 4
	else:
		if showing > 0:
			showing = (showing*10) + 4
		else:
			showing = 4
	display = Label(window,text=showing)
	display.grid(row=0,column = 3)
def but5():
	global showing
	global ans
	if ans == 0:
		showing = 5
		ans = 5
	else:
		if showing > 0:
			showing = (showing*10) + 5
		else:
			showing = 5
	display = Label(window,text=showing)
	display.grid(row=0,column = 3)
def but6():
	global showing
	global ans
	if ans == 0:
		showing = 6
		ans = 6
	else:
		if showing > 0:
			showing = (showing*10) + 6
		else:
			showing = 6
	display = Label(window,text=showing)
	display.grid(row=0,column = 3)
def but7():
	global showing
	global ans
	if ans == 0:
		showing = 7
		ans = 7
	else:
		if showing > 0:
			showing = (showing*10) + 7
		else:
			showing = 7
	display = Label(window,text=showing)
	display.grid(row=0,column = 3)
def but8():
	global showing
	global ans
	if ans == 0:
		showing = 8
		ans = 8
	else:
		if showing > 0:
			showing = (showing*10) + 8
		else:
			showing = 8
	display = Label(window,text=showing)
	display.grid(row=0,column = 3)
def but9():
	global showing
	global ans
	if ans == 0:
		showing = 9
		ans = 9
	else:
		if showing > 0:
			showing = (showing*10) + 9
		else:
			showing = 9
	display = Label(window,text=showing)
	display.grid(row=0,column = 3)
def but10():
	global showing
	global ans
	if ans == 0:
		showing = 0
		ans = 0
	else:
		if showing > 0:
			showing = (showing*10)
		else:
			showing = 0
	display = Label(window,text=showing)
	display.grid(row=0,column = 3)
def but11():
	global showing
	if type(showing) is not float:
		showing = showing * 1.0
	display = Label(window,text=showing)
	display.grid(row=0,column = 3)
def but12():
	global showing
	global ans
	global curfunc
	print ans,curfunc,showing
	if curfunc == '+':
		ans = ans + showing
	elif curfunc == '-':
		ans = ans - showing
	elif curfunc == '*':
		ans = ans * showing
	elif curfunc == '/':
		if ans % showing == 0:
			ans = ans / showing
		else:
			ans = ans*1.0 / showing
	showing = ans
	display = Label(window,text=showing)
	display.grid(row=0,column = 3)
def but13():
	global curfunc
	global showing
	global ans
	curfunc = '+'
	ans = showing
	showing = 0
	display = Label(window,text=showing)
	display.grid(row=0,column = 3)
def but14():
	global curfunc
	global showing
	global ans
	curfunc = '-'
	ans = showing
	showing = 0
	display = Label(window,text=showing)
	display.grid(row=0,column = 3)
def but15():
	global curfunc
	global showing
	global ans
	curfunc = '*'
	ans = showing
	showing = 0
	display = Label(window,text=showing)
	display.grid(row=0,column = 3)
def but16():
	global curfunc
	global showing
	global ans
	curfunc = '/'
	ans = showing
	showing = 0
	display = Label(window,text=showing)
	display.grid(row=0,column = 3)

b1.configure(command=but1)
b2.configure(command=but2)
b3.configure(command=but3)
b4.configure(command=but4)
b5.configure(command=but5)
b6.configure(command=but6)
b7.configure(command=but7)
b8.configure(command=but8)
b9.configure(command=but9)
b10.configure(command=but10)
b11.configure(command=but11)
b12.configure(command=but12)
b13.configure(command=but13)
b14.configure(command=but14)
b15.configure(command=but15)
b16.configure(command=but16)
frame1 = Frame(window)
display = Label(window,text=showing)
display.grid(row=0,column = 3)
window.mainloop()
