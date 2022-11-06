from tkinter import Tk, PhotoImage, Button, messagebox, Canvas, Entry
import os
rectangle = [None]*9
def level1b():
	rectangle[0] = Button(window, image=OB, width="200", height="100", command=page1b)
	rectangle[0].place(x=70, y=300)
def level1bb():
	rectangle[0] = Button(window, width="200", height="100", command=lambda: handle_button_click(0))
	rectangle[0].place(x=70, y=300)
def level1w():
	rectangle[0] = Button(window, image=OW, width="200", height="100", command=page1w)
	rectangle[0].place(x=370, y=300)
def level1wb():
	rectangle[0] = Button(window, width="200", height="100", command=lambda: handle_button_click(0))
	rectangle[0].place(x=370, y=300)
def level1Lb():
	rectangle[0] = Button(window, image=SavOB, width="200", height="100", command=page1bL)
	rectangle[0].place(x=670, y=300)
def level1Lbb():
	rectangle[0] = Button(window, width="200", height="100", command=lambda: handle_button_click(0))
	rectangle[0].place(x=670, y=300)
def level1Lw():
	rectangle[0] = Button(window, image=SavOW, width="200", height="100", command=page1wL)
	rectangle[0].place(x=970, y=300)
def level1Lwb():
	rectangle[0] = Button(window, width="200", height="100", command=lambda: handle_button_click(0))
	rectangle[0].place(x=970, y=300)
def leaderborad():
	rectangle[0] = Button(window, image=Lead, width="500", height="50", command=Lpage)
	rectangle[0].place(x=70, y=650)
def leaderboradb():
	rectangle[0] = Button(window, width="500", height="50", command=lambda: handle_button_click(0))
	rectangle[0].place(x=70, y=650)
def Quit():
	rectangle[0] = Button(window, image=quit, width="100", height="50", command=close)
	rectangle[0].place(x=970, y=650)
def Quitb():
	rectangle[0] = Button(window, width="100", height="50", command=lambda: handle_button_click(0))
	rectangle[0].place(x=970, y=650)

def Lpage():
	window = Tk()
	window.title("leaderborad")
	window.geometry("1280x720")
	canvas = Canvas(window, width=1280, height=720, bg="black")
	canvas.pack()
	T1 = canvas.create_text(640, 100, font = ("Purisa", 30), text= "Level 1")
	f = open("Leader1.txt", "r")
	Score1L1 = f.readline()
	Score1L2 = f.readline()
	Score1L3 = f.readline()
	Score1L4 = f.readline()
	Score1L5 = f.readline()
	Label1 = canvas.create_text(640, 300, font = ("Purisa", 30), text=(str(Score1L1) + "\n" + str(Score1L2) + "\n" + str(Score1L3) + "\n" + str(Score1L4) + "\n" + str(Score1L5)))
	f.close()

def close():
	window.destroy()

def page1b():
	class Ball:
		def __init__(B, canvas, bar11, bar22):
			B.canvas = canvas
			B.bar11 = bar11
			B.bar22 = bar22
			size = 50
			B.shape = canvas.create_rectangle(75, 75, size, size, fill="white")
			B.canvas.move(B.shape, 10, 10)
			B.xspeed = 1
			B.yspeed = 1
			B.run = 1
			B.score = 0

		def bounce(B):
			global posB, bar2pos, bar1pos, Score1
			B.canvas.move(B.shape, B.xspeed, B.yspeed)
			bar1pos = B.canvas.coords(B.bar11.shape)
			posB = B.canvas.coords(B.shape)
			bar2pos = B.canvas.coords(B.bar22.shape)
			Score1 = B.score
			if posB[1] <= 0:
				B.yspeed = 3
				if B.score > 5:
					B.yspeed = 5.5
					if B.score > 10:
						B.yspeed = 10
			if posB[3] >= 720:
				B.yspeed = -3
				if B.score > 5:
					B.yspeed = -5.5
					if B.score > 10:
						B.yspeed = -10

			if posB[0] <= 0:
				B.score = B.score - 1
				canvas.delete(B.shape)
				size = 50
				B.shape = canvas.create_rectangle(75 + 900, 75 + 10, size + 900, size + 10, fill="white")
				B.canvas.move(B.shape, -10, 10)	
			elif posB[0] >= 1280:
				B.score = B.score + 1
				canvas.delete(B.shape)
				size = 50
				B.shape = canvas.create_rectangle(75, 75, size, size, fill="white")
				B.canvas.move(B.shape, 10, 10)
			if posB[2] >= 1280:
				B.score = B.score + 1
				canvas.delete(B.shape)
				size = 50
				B.shape = canvas.create_rectangle(75, 75, size, size, fill="white")
				B.canvas.move(B.shape, 10, 10)
			elif posB[2] <= 0:
				B.score = B.score - 1
				canvas.delete(B.shape)
				size = 50
				B.shape = canvas.create_rectangle(75 + 900, 75 + 10, size + 900, size + 10, fill="white")
				B.canvas.move(B.shape, -10, 10)
			if B.hitbar1(posB) == True:
				B.xspeed = 3
				# B.score = B.score + 1
			if B.hitbar2(posB) == True:
				B.xspeed = -3
		
		def hitbar1(B, posB):
			bar1pos = B.canvas.coords(B.bar11.shape)
			if (posB[2]) >= bar1pos[0] and posB[0] <= bar1pos[2]:
				if (posB[3]) >= bar1pos[1] and posB[1] <= bar1pos[3]:
					return True
			bar1pos.clear()
			return False

		def hitbar2(B, posB):
			bar2pos = B.canvas.coords(B.bar22.shape)
			if (posB[2]) >= bar2pos[0] and (posB[0]) <= (bar2pos[2]):
				if posB[3] >= bar2pos[1] and posB[1] <= bar2pos[3]:
					return True
			bar2pos.clear()
			return False

		def Amove_bar2(B, posB):
			if bar2pos[3] >= 720:
				bar22.yspeed = 0
			if bar2pos[1] <= posB[1]:
				bar22.yspeed = 2
				if B.score > 5:
					bar22.yspeed = 4.7
					if B.score > 10:
						bar22.yspeed = 9.8
			elif bar2pos[3] >= posB[3]:
				bar22.yspeed = -2
				if B.score > 5:
					bar22.yspeed = -4.7
					if B.score > 10:
						bar22.yspeed = -9.8



	class Bar1:
		def __init__(bar1, canvas):
			bar1.canvas = canvas
			bar1Size = 8
			bar1.shape = canvas.create_rectangle(bar1Size, bar1Size + 360, (bar1Size * 2), (bar1Size * 8) + 360, fill="white")
			bar1.yspeed = 0
			bar1.canvas.bind_all('<KeyPress-Up>', bar1.move_up1)
			bar1.canvas.bind_all('<KeyPress-Down>', bar1.move_down1)
			bar1.canvas.bind_all('<KeyPress-w>', bar1.cheatU)
			bar1.canvas.bind_all('<KeyPress-s>', bar1.cheatD)

		def move_bar1(bar1):
			bar1.canvas.move(bar1.shape, 0, bar1.yspeed)
			pos1 = bar1.canvas.coords(bar1.shape)
			if pos1[1] <= 0:
				bar1.yspeed = 0
			if pos1[3] >= 720:
				bar1.yspeed = 0

		def move_up1(bar1, event):
			bar1.yspeed = -2
		def move_down1(bar1, event):
			bar1.yspeed = 2

		def cheatD(bar1, event):
			bar1.yspeed = 10
		def cheatU(bar1, event):
			bar1.yspeed = -10

	class Bar2:
		def __init__(bar2, canvas):
			bar2.canvas = canvas
			bar2Size = 8
			bar2.shape = canvas.create_rectangle(bar2Size + 1260, bar2Size + 360, (bar2Size * 2) + 1260, (bar2Size * 8) + 360, fill="white")
			bar2.yspeed = 0

		def move_bar2(bar2):
			bar2.canvas.move(bar2.shape, 0, bar2.yspeed)
			pos2 = bar2.canvas.coords(bar2.shape)
			if pos2[1] <= 0:
				bar2.yspeed = 0
			if pos2[3] >= 720:
				bar2.yspeed = 0

		def move_up2(bar2, event):
			bar2.yspeed = -2
		def move_down2(bar2, event):
			bar2.yspeed = 2
	
	class PButton:
		def __init__(p, canvas, Button):
			p.canvas = canvas
			p.button = Button
			p.button = Button(window, width ="2", height="1", command=Stop, text="Pause")
			p.button.place(x=0, y=0)
	
	class RButton:
		def __init__(r, canvas, Button):
			r.canvas = canvas
			r.button = Button
			r.button = Button(window, width="2", height="1", command=resume, text="Resume")
			r.button.place(x=100, y=0)

	class Load:
		def __init__(L, canvas, Button):
			L.canvas = canvas
			L.button = Button
			L.button = Button(window, width="2", height="1", command=store, text="Save")
			L.button.place(x=200, y=0)

	class ReturnC:
		def __init__(HC, canvas, Button):
			HC.canvas = canvas
			HC.button = Button
			HC.button = Button(window, width="2", height="1", command=mainC, text="Quit")
			HC.button.place(x=300, y=0)

	class ChangeB:
		def __init__(C, canvas, Button):
			C.canvas = canvas
			C.button = Button
			C.button = Button(window, width="2", height="1", command=Change, text="B")
			C.button.place(x=400, y=0)

	def resume():
		ball.run = 1
	def Stop():
		ball.run = 0
	def store():
		window = Tk()
		window.title("Name")
		window.geometry('400x300')
		def printValue():
			global text
			pname = player_name.get()
			text = f'{pname}'
		player_name = Entry(window)
		player_name.pack(pady=30)
		Button(window, text="Register Player",padx=10, pady=5,command=printValue).pack()
		window.mainloop()
		print(text)
		f = open("testing.txt", "w")
		f.write(str(text) + " " + str(Score1) + " " + "\n" + str(posB[0]) + " " + str(posB[1]) + " " + str(posB[2]) + " " + str(posB[3]) + "\n" + str(bar2pos[0]) + " " + str(bar2pos[1]) + " " + str(bar2pos[2]) + " " + str(bar2pos[3]) + "\n" + str(bar1pos[0]) + " " + str(bar1pos[1]) + " " + str(bar1pos[2]) + " " + str(bar1pos[3]))
		f.close()
		f = open("Leader1.txt", "r")
		content = f.read()
		print(content)
		f = open("dummy.txt", "w")
		f.write(str(text) + " " + str(Score1) + " " + "\n" + content)
		f.close()
		os.remove("Leader1.txt")
		os.rename("dummy.txt", "Leader1.txt")
	def mainC():
		window.destroy()

	def Change():   
		window = Tk()
		window.title("Home")
		canvas = Canvas(window, width=1280, height=720, bg="black")
		canvas.pack()


	window = Tk()
	window.title("Ping Pong1")
	width = 1280
	height= 720
	canvas = Canvas(window, width=1280, height=720, bg="black")
	canvas.pack()
	label = canvas.create_text(640, 20, font = ("Purisa", 30), text="Score: 0")
	window.update()
	bar11 = Bar1(canvas)
	bar22 = Bar2(canvas)
	ball = Ball(canvas, bar11, bar22)
	Pause = PButton(canvas, Button)
	Resume = RButton(canvas, Button)
	DataO = Load(canvas, Button)
	HomeC = ReturnC(canvas, Button)
	HomeB = ChangeB(canvas, Button)
	while True:
		if ball.run == 1:
			bar11.move_bar1()
			bar22.move_bar2()
			ball.bounce()
			ball.Amove_bar2(posB)
			canvas.itemconfig(label, text="Score: "+ str(Score1))
			window.update_idletasks()
			window.update()
		elif ball.run == 0:
			window.update_idletasks()
			window.update()
	window.update()

def page1bL():
	global positionB, positionB2, positionB1
	f = open("testing.txt", "r")
	Score1L = f.readline()
	positionB = f.readline()
	positionB2 = f.readline()
	positionB1 = f.readline()
	Score1L = Score1L.split()
	Score1L = Score1L[1]
	positionB = positionB.split()
	positionB2 = positionB2.split()
	positionB1 = positionB1.split()
	print(positionB)
	print(positionB2)
	print(positionB1)
	class Ball:
		def __init__(B, canvas, bar11, bar22):
			B.canvas = canvas
			B.bar11 = bar11
			B.bar22 = bar22
			size = 50
			B.shape = canvas.create_rectangle(positionB[0], positionB[1], positionB[2], positionB[3], fill="white")
			B.canvas.move(B.shape, 10, 10)
			B.xspeed = 1
			B.yspeed = 1
			B.run = 1
			B.score = Score1L

		def bounce(B):
			global posB, bar2pos, bar1pos, Score1
			B.canvas.move(B.shape, B.xspeed, B.yspeed)
			bar1pos = B.canvas.coords(B.bar11.shape)
			posB = B.canvas.coords(B.shape)
			bar2pos = B.canvas.coords(B.bar22.shape)
			Score1L = int(B.score)
			if posB[1] <= 0:
				B.yspeed = 3
				if int(B.score) > 5:
					B.yspeed = 5.5
					if int(B.score) > 10:
						B.yspeed = 10
			if posB[3] >= 720:
				B.yspeed = -3
				if int(B.score) > 5:
					B.yspeed = -5.5
					if int(B.score) > 10:
						B.yspeed = -10
			if posB[0] <= 0:
				B.score = int(B.score) - 1
				canvas.delete(B.shape)
				size = 50
				B.shape = canvas.create_rectangle(75 + 900, 75 + 10, size + 900, size + 10, fill="white")
				B.canvas.move(B.shape, -10, 10)	
			elif posB[0] >= 1280:
				B.score = int(B.score) + 1
				canvas.delete(B.shape)
				size = 50
				B.shape = canvas.create_rectangle(75, 75, size, size, fill="white")
				B.canvas.move(B.shape, 10, 10)
			if posB[2] >= 1280:
				B.score = int(B.score) + 1
				canvas.delete(B.shape)
				size = 50
				B.shape = canvas.create_rectangle(75, 75, size, size, fill="white")
				B.canvas.move(B.shape, 10, 10)
			elif posB[2] <= 0:
				B.score = int(B.score) - 1
				canvas.delete(B.shape)
				size = 50
				B.shape = canvas.create_rectangle(75 + 900, 75 + 10, size + 900, size + 10, fill="white")
				B.canvas.move(B.shape, -10, 10)
			if B.hitbar1(posB) == True:
				B.xspeed = 3
			if B.hitbar2(posB) == True:
				B.xspeed = -3
		
		def hitbar1(B, posB):
			bar1pos = B.canvas.coords(B.bar11.shape)
			if (posB[2]) >= bar1pos[0] and posB[0] <= bar1pos[2]:
				if (posB[3]) >= bar1pos[1] and posB[1] <= bar1pos[3]:
					return True
			bar1pos.clear()
			return False

		def hitbar2(B, posB):
			bar2pos = B.canvas.coords(B.bar22.shape)
			if (posB[2]) >= bar2pos[0] and (posB[0]) <= (bar2pos[2]):
				if posB[3] >= bar2pos[1] and posB[1] <= bar2pos[3]:
					return True
			bar2pos.clear()
			return False

		def Amove_bar2(B, posB):
			if bar2pos[1] <= posB[1]:
				bar22.yspeed = 2
				if int(B.score) > 5:
					bar22.yspeed = 4.7
					if int(B.score) > 10:
						bar22.yspeed = 9.8
			elif bar2pos[3] >= posB[3]:
				bar22.yspeed = -2
				if int(B.score)> 5:
					bar22.yspeed = -4.7
					if int(B.score) > 10:
						bar22.yspeed = -9.8



	class Bar1:
		def __init__(bar1, canvas):
			bar1.canvas = canvas
			bar1Size = 8
			bar1.shape = canvas.create_rectangle(positionB1[0], positionB1[1], positionB1[2], positionB1[3], fill="white")
			bar1.yspeed = 0
			bar1.canvas.bind_all('<KeyPress-Up>', bar1.move_up1)
			bar1.canvas.bind_all('<KeyPress-Down>', bar1.move_down1)
			bar1.canvas.bind_all('<KeyPress-w>', bar1.cheatU)
			bar1.canvas.bind_all('<KeyPress-s>', bar1.cheatD)

		def move_bar1(bar1):
			bar1.canvas.move(bar1.shape, 0, bar1.yspeed)
			pos1 = bar1.canvas.coords(bar1.shape)
			if pos1[1] <= 0:
				bar1.yspeed = 0
			if pos1[3] >= 720:
				bar1.yspeed = 0

		def move_up1(bar1, event):
			bar1.yspeed = -2
		def move_down1(bar1, event):
			bar1.yspeed = 2

		def cheatD(bar1, event):
			bar1.yspeed = 10
		def cheatU(bar1, event):
			bar1.yspeed = -10

	class Bar2:
		def __init__(bar2, canvas):
			bar2.canvas = canvas
			bar2Size = 8
			bar2.shape = canvas.create_rectangle(positionB2[0], positionB2[1], positionB2[2], positionB2[3], fill="white")
			bar2.yspeed = 0

		def move_bar2(bar2):
			bar2.canvas.move(bar2.shape, 0, bar2.yspeed)
			pos2 = bar2.canvas.coords(bar2.shape)
			if pos2[1] <= 0:
				bar2.yspeed = 0
			if pos2[3] >= 720:
				bar2.yspeed = 0

		def move_up2(bar2, event):
			bar2.yspeed = -2
		def move_down2(bar2, event):
			bar2.yspeed = 2
	
	class PButton:
		def __init__(p, canvas, Button):
			p.canvas = canvas
			p.button = Button
			p.button = Button(window, width ="2", height="1", command=Stop, text="Pause")
			p.button.place(x=0, y=0)
	
	class RButton:
		def __init__(r, canvas, Button):
			r.canvas = canvas
			r.button = Button
			r.button = Button(window, width="2", height="1", command=resume, text="Resume")
			r.button.place(x=100, y=0)

	class Load:
		def __init__(L, canvas, Button):
			L.canvas = canvas
			L.button = Button
			L.button = Button(window, width="2", height="1", command=store, text="Save")
			L.button.place(x=200, y=0)

	class ReturnC:
		def __init__(HC, canvas, Button):
			HC.canvas = canvas
			HC.button = Button
			HC.button = Button(window, width="2", height="1", command=mainC, text="Quit")
			HC.button.place(x=300, y=0)

	class ChangeB:
		def __init__(C, canvas, Button):
			C.canvas = canvas
			C.button = Button
			C.button = Button(window, width="2", height="1", command=Change, text="B")
			C.button.place(x=400, y=0)

	def resume():
		ball.run = 1
	def Stop():
		ball.run = 0
	def store():
		window = Tk()
		window.title("Name")
		window.geometry('400x300')
		def printValue():
			global text
			pname = player_name.get()
			text = f'{pname}'
		player_name = Entry(window)
		player_name.pack(pady=30)
		Button(window, text="Register Player",padx=10, pady=5,command=printValue).pack()
		window.mainloop()
		print(text)
		f = open("testing.txt", "w")
		f.write(str(text) + " " + str(Score1L) + " " + "\n" + str(posB[0]) + " " + str(posB[1]) + " " + str(posB[2]) + " " + str(posB[3]) + "\n" + str(bar2pos[0]) + " " + str(bar2pos[1]) + " " + str(bar2pos[2]) + " " + str(bar2pos[3]) + "\n" + str(bar1pos[0]) + " " + str(bar1pos[1]) + " " + str(bar1pos[2]) + " " + str(bar1pos[3]))
		f.close()
		f = open("Leader1.txt", "r")
		content = f.read()
		print(content)
		f = open("dummy.txt", "w")
		f.write(str(text) + " " + str(Score1L) + " " + "\n" + content)
		f.close()
		os.remove("Leader1.txt")
		os.rename("dummy.txt", "Leader1.txt")
	def mainC():
		window.destroy()

	def Change():   
		window = Tk()
		window.title("Home")
		canvas = Canvas(window, width=1280, height=720, bg="black")
		canvas.pack()


	window = Tk()
	window.title("Ping Pong1")
	width = 1280
	height= 720
	canvas = Canvas(window, width=1280, height=720, bg="black")
	canvas.pack()
	label = canvas.create_text(640, 20, font = ("Purisa", 30), text="Score: 0")
	window.update()
	bar11 = Bar1(canvas)
	bar22 = Bar2(canvas)
	ball = Ball(canvas, bar11, bar22)
	Pause = PButton(canvas, Button)
	Resume = RButton(canvas, Button)
	DataO = Load(canvas, Button)
	HomeC = ReturnC(canvas, Button)
	HomeB = ChangeB(canvas, Button)
	while True:
		if ball.run == 1:
			bar11.move_bar1()
			bar22.move_bar2()
			ball.bounce()
			ball.Amove_bar2(posB)
			canvas.itemconfig(label, text="Score: "+ str(Score1L))
			window.update_idletasks()
			window.update()
		elif ball.run == 0:
			window.update_idletasks()
			window.update()
	window.update()

def page1w():
	class Ball:
		def __init__(B, canvas, bar11, bar22):
			B.canvas = canvas
			B.bar11 = bar11
			B.bar22 = bar22
			size = 50
			B.shape = canvas.create_rectangle(75, 75, size, size, fill="black")
			B.canvas.move(B.shape, 10, 10)
			B.xspeed = 1
			B.yspeed = 1
			B.run = 1
			B.score = 0

		def bounce(B):
			global posB, bar2pos, bar1pos, Score1
			B.canvas.move(B.shape, B.xspeed, B.yspeed)
			bar1pos = B.canvas.coords(B.bar11.shape)
			posB = B.canvas.coords(B.shape)
			bar2pos = B.canvas.coords(B.bar22.shape)
			Score1 = B.score
			if posB[1] <= 0:
				B.yspeed = 3
				if B.score > 5:
					B.yspeed = 5.5
					if B.score > 10:
						B.yspeed = 10
			if posB[3] >= 720:
				B.yspeed = -3
				if B.score > 5:
					B.yspeed = -5.5
					if B.score > 10:
						B.yspeed = -10
			if posB[0] <= 0:
				B.score = B.score - 1
				canvas.delete(B.shape)
				size = 50
				B.shape = canvas.create_rectangle(75 + 900, 75 + 10, size + 900, size + 10, fill="white")
				B.canvas.move(B.shape, -10, 10)	
			elif posB[0] >= 1280:
				B.score = B.score + 1
				canvas.delete(B.shape)
				size = 50
				B.shape = canvas.create_rectangle(75, 75, size, size, fill="white")
				B.canvas.move(B.shape, 10, 10)
			if posB[2] >= 1280:
				B.score = B.score + 1
				canvas.delete(B.shape)
				size = 50
				B.shape = canvas.create_rectangle(75, 75, size, size, fill="white")
				B.canvas.move(B.shape, 10, 10)
			elif posB[2] <= 0:
				B.score = B.score - 1
				canvas.delete(B.shape)
				size = 50
				B.shape = canvas.create_rectangle(75 + 900, 75 + 10, size + 900, size + 10, fill="white")
				B.canvas.move(B.shape, -10, 10)
			if B.hitbar1(posB) == True:
				B.xspeed = 3
			if B.hitbar2(posB) == True:
				B.xspeed = -3
		
		def hitbar1(B, posB):
			bar1pos = B.canvas.coords(B.bar11.shape)
			if (posB[2]) >= bar1pos[0] and posB[0] <= bar1pos[2]:
				if (posB[3]) >= bar1pos[1] and posB[1] <= bar1pos[3]:
					return True
			bar1pos.clear()
			return False

		def hitbar2(B, posB):
			bar2pos = B.canvas.coords(B.bar22.shape)
			if (posB[2]) >= bar2pos[0] and (posB[0]) <= (bar2pos[2]):
				if posB[3] >= bar2pos[1] and posB[1] <= bar2pos[3]:
					return True
			bar2pos.clear()
			return False

		def Amove_bar2(B, posB):
			if bar2pos[3] >= 720:
				bar22.yspeed = 0
			if bar2pos[1] <= posB[1]:
				bar22.yspeed = 2
				if B.score > 5:
					bar22.yspeed = 4.7
					if B.score > 10:
						bar22.yspeed = 9.8
			elif bar2pos[3] >= posB[3]:
				bar22.yspeed = -2
				if B.score > 5:
					bar22.yspeed = -4.7
					if B.score > 10:
						bar22.yspeed = -9.8



	class Bar1:
		def __init__(bar1, canvas):
			bar1.canvas = canvas
			bar1Size = 8
			bar1.shape = canvas.create_rectangle(bar1Size, bar1Size + 360, (bar1Size * 2), (bar1Size * 8) + 360, fill="black")
			bar1.yspeed = 0
			bar1.canvas.bind_all('<KeyPress-Up>', bar1.move_up1)
			bar1.canvas.bind_all('<KeyPress-Down>', bar1.move_down1)
			bar1.canvas.bind_all('<KeyPress-w>', bar1.cheatU)
			bar1.canvas.bind_all('<KeyPress-s>', bar1.cheatD)

		def move_bar1(bar1):
			bar1.canvas.move(bar1.shape, 0, bar1.yspeed)
			pos1 = bar1.canvas.coords(bar1.shape)
			if pos1[1] <= 0:
				bar1.yspeed = 0
			if pos1[3] >= 720:
				bar1.yspeed = 0

		def move_up1(bar1, event):
			bar1.yspeed = -2
		def move_down1(bar1, event):
			bar1.yspeed = 2

		def cheatD(bar1, event):
			bar1.yspeed = 10
		def cheatU(bar1, event):
			bar1.yspeed = -10

	class Bar2:
		def __init__(bar2, canvas):
			bar2.canvas = canvas
			bar2Size = 8
			bar2.shape = canvas.create_rectangle(bar2Size + 1260, bar2Size + 360, (bar2Size * 2) + 1260, (bar2Size * 8) + 360, fill="black")
			bar2.yspeed = 0

		def move_bar2(bar2):
			bar2.canvas.move(bar2.shape, 0, bar2.yspeed)
			pos2 = bar2.canvas.coords(bar2.shape)
			if pos2[1] <= 0:
				bar2.yspeed = 0
			if pos2[3] >= 720:
				bar2.yspeed = 0

		def move_up2(bar2, event):
			bar2.yspeed = -2
		def move_down2(bar2, event):
			bar2.yspeed = 2
	
	class PButton:
		def __init__(p, canvas, Button):
			p.canvas = canvas
			p.button = Button
			p.button = Button(window, width ="2", height="1", command=Stop, text="Pause")
			p.button.place(x=0, y=0)
	
	class RButton:
		def __init__(r, canvas, Button):
			r.canvas = canvas
			r.button = Button
			r.button = Button(window, width="2", height="1", command=resume, text="Resume")
			r.button.place(x=100, y=0)

	class Load:
		def __init__(L, canvas, Button):
			L.canvas = canvas
			L.button = Button
			L.button = Button(window, width="2", height="1", command=store, text="Save")
			L.button.place(x=200, y=0)

	class ReturnC:
		def __init__(HC, canvas, Button):
			HC.canvas = canvas
			HC.button = Button
			HC.button = Button(window, width="2", height="1", command=mainC, text="Quit")
			HC.button.place(x=300, y=0)

	class ChangeB:
		def __init__(C, canvas, Button):
			C.canvas = canvas
			C.button = Button
			C.button = Button(window, width="2", height="1", command=Change, text="B")
			C.button.place(x=400, y=0)

	def resume():
		ball.run = 1
	def Stop():
		ball.run = 0
	def store():
		window = Tk()
		window.title("Name")
		window.geometry('400x300')
		def printValue():
			global text
			pname = player_name.get()
			text = f'{pname}'
		player_name = Entry(window)
		player_name.pack(pady=30)
		Button(window, text="Register Player",padx=10, pady=5,command=printValue).pack()
		window.mainloop()
		print(text)
		f = open("testing.txt", "w")
		f.write(str(text) + " " + str(Score1) + " " + "\n" + str(posB[0]) + " " + str(posB[1]) + " " + str(posB[2]) + " " + str(posB[3]) + "\n" + str(bar2pos[0]) + " " + str(bar2pos[1]) + " " + str(bar2pos[2]) + " " + str(bar2pos[3]) + "\n" + str(bar1pos[0]) + " " + str(bar1pos[1]) + " " + str(bar1pos[2]) + " " + str(bar1pos[3]))
		f.close()
		f = open("Leader1.txt", "r")
		content = f.read()
		print(content)
		f = open("dummy.txt", "w")
		f.write(str(text) + " " + str(Score1) + " " + "\n" + content)
		f.close()
		os.remove("Leader1.txt")
		os.rename("dummy.txt", "Leader1.txt")
	def mainC():
		window.destroy()

	def Change():   
		window = Tk()
		window.title("Home")
		canvas = Canvas(window, width=1280, height=720, bg="black")
		canvas.pack()


	window = Tk()
	window.title("Ping Pong1")
	width = 1280
	height= 720
	canvas = Canvas(window, width=1280, height=720, bg="white")
	canvas.pack()
	label = canvas.create_text(640, 20, font = ("Purisa", 30), text="Score: 0")
	window.update()
	bar11 = Bar1(canvas)
	bar22 = Bar2(canvas)
	ball = Ball(canvas, bar11, bar22)
	Pause = PButton(canvas, Button)
	Resume = RButton(canvas, Button)
	DataO = Load(canvas, Button)
	HomeC = ReturnC(canvas, Button)
	HomeB = ChangeB(canvas, Button)
	while True:
		if ball.run == 1:
			bar11.move_bar1()
			bar22.move_bar2()
			ball.bounce()
			ball.Amove_bar2(posB)
			canvas.itemconfig(label, text="Score: "+ str(Score1))
			window.update_idletasks()
			window.update()
		elif ball.run == 0:
			window.update_idletasks()
			window.update()
	window.update()

def page1wL():
	global positionB, positionB2, positionB1
	f = open("testing.txt", "r")
	Score1L = f.readline()
	positionB = f.readline()
	positionB2 = f.readline()
	positionB1 = f.readline()
	Score1L = Score1L.split()
	Score1L = Score1L[1]
	positionB = positionB.split()
	positionB2 = positionB2.split()
	positionB1 = positionB1.split()
	print(Score1L)
	print(positionB)
	print(positionB2)
	print(positionB1)
	class Ball:
		def __init__(B, canvas, bar11, bar22):
			B.canvas = canvas
			B.bar11 = bar11
			B.bar22 = bar22
			size = 50
			B.shape = canvas.create_rectangle(positionB[0], positionB[1], positionB[2], positionB[3], fill="black")
			B.canvas.move(B.shape, 10, 10)
			B.xspeed = 1
			B.yspeed = 1
			B.run = 1
			B.score = Score1L

		def bounce(B):
			global posB, bar2pos, bar1pos, Score1
			B.canvas.move(B.shape, B.xspeed, B.yspeed)
			bar1pos = B.canvas.coords(B.bar11.shape)
			posB = B.canvas.coords(B.shape)
			bar2pos = B.canvas.coords(B.bar22.shape)
			Score1L = int(B.score)
			if posB[1] <= 0:
				B.yspeed = 3
				if int(B.score) > 5:
					B.yspeed = 5.5
					if int(B.score) > 10:
						B.yspeed = 10
			if posB[3] >= 720:
				B.yspeed = -3
				if int(B.score) > 5:
					B.yspeed = -5.5
					if int(B.score) > 10:
						B.yspeed = -10
			if posB[0] <= 0:
				B.score = int(B.score) - 1
				canvas.delete(B.shape)
				size = 50
				B.shape = canvas.create_rectangle(75 + 900, 75 + 10, size + 900, size + 10, fill="white")
				B.canvas.move(B.shape, -10, 10)	
			elif posB[0] >= 1280:
				B.score = int(B.score) + 1
				canvas.delete(B.shape)
				size = 50
				B.shape = canvas.create_rectangle(75, 75, size, size, fill="white")
				B.canvas.move(B.shape, 10, 10)
			if posB[2] >= 1280:
				B.score = int(B.score) + 1
				canvas.delete(B.shape)
				size = 50
				B.shape = canvas.create_rectangle(75, 75, size, size, fill="white")
				B.canvas.move(B.shape, 10, 10)
			elif posB[2] <= 0:
				B.score = int(B.score) - 1
				canvas.delete(B.shape)
				size = 50
				B.shape = canvas.create_rectangle(75 + 900, 75 + 10, size + 900, size + 10, fill="white")
				B.canvas.move(B.shape, -10, 10)
			if B.hitbar1(posB) == True:
				B.xspeed = 3
			if B.hitbar2(posB) == True:
				B.xspeed = -3
		
		def hitbar1(B, posB):
			bar1pos = B.canvas.coords(B.bar11.shape)
			if (posB[2]) >= bar1pos[0] and posB[0] <= bar1pos[2]:
				if (posB[3]) >= bar1pos[1] and posB[1] <= bar1pos[3]:
					return True
			bar1pos.clear()
			return False

		def hitbar2(B, posB):
			bar2pos = B.canvas.coords(B.bar22.shape)
			if (posB[2]) >= bar2pos[0] and (posB[0]) <= (bar2pos[2]):
				if posB[3] >= bar2pos[1] and posB[1] <= bar2pos[3]:
					return True
			bar2pos.clear()
			return False

		def Amove_bar2(B, posB):
			Score1L = B.score
			if bar2pos[3] >= 720:
				bar22.yspeed = 0
			if bar2pos[1] <= posB[1]:
				bar22.yspeed = 2
				if int(B.score) > 5:
					bar22.yspeed = 4.7
					if int(B.score) > 10:
						bar22.yspeed = 9.8
			elif bar2pos[3] >= posB[3]:
				bar22.yspeed = -2
				if int(B.score) > 5:
					bar22.yspeed = -4.7
					if int(B.score) > 10:
						bar22.yspeed = -9.8



	class Bar1:
		def __init__(bar1, canvas):
			bar1.canvas = canvas
			bar1Size = 8
			bar1.shape = canvas.create_rectangle(positionB1[0], positionB1[1], positionB1[2], positionB1[3], fill="black")
			bar1.yspeed = 0
			bar1.canvas.bind_all('<KeyPress-Up>', bar1.move_up1)
			bar1.canvas.bind_all('<KeyPress-Down>', bar1.move_down1)
			bar1.canvas.bind_all('<KeyPress-w>', bar1.cheatU)
			bar1.canvas.bind_all('<KeyPress-s>', bar1.cheatD)

		def move_bar1(bar1):
			bar1.canvas.move(bar1.shape, 0, bar1.yspeed)
			pos1 = bar1.canvas.coords(bar1.shape)
			if pos1[1] <= 0:
				bar1.yspeed = 0
			if pos1[3] >= 720:
				bar1.yspeed = 0

		def move_up1(bar1, event):
			bar1.yspeed = -2
		def move_down1(bar1, event):
			bar1.yspeed = 2

		def cheatD(bar1, event):
			bar1.yspeed = 10
		def cheatU(bar1, event):
			bar1.yspeed = -10

	class Bar2:
		def __init__(bar2, canvas):
			bar2.canvas = canvas
			bar2Size = 8
			bar2.shape = canvas.create_rectangle(positionB2[0], positionB2[1], positionB2[2], positionB2[3], fill="black")
			bar2.yspeed = 0

		def move_bar2(bar2):
			bar2.canvas.move(bar2.shape, 0, bar2.yspeed)
			pos2 = bar2.canvas.coords(bar2.shape)
			if pos2[1] <= 0:
				bar2.yspeed = 0
			if pos2[3] >= 720:
				bar2.yspeed = 0

		def move_up2(bar2, event):
			bar2.yspeed = -2
		def move_down2(bar2, event):
			bar2.yspeed = 2
	
	class PButton:
		def __init__(p, canvas, Button):
			p.canvas = canvas
			p.button = Button
			p.button = Button(window, width ="2", height="1", command=Stop, text="Pause")
			p.button.place(x=0, y=0)
	
	class RButton:
		def __init__(r, canvas, Button):
			r.canvas = canvas
			r.button = Button
			r.button = Button(window, width="2", height="1", command=resume, text="Resume")
			r.button.place(x=100, y=0)

	class Load:
		def __init__(L, canvas, Button):
			L.canvas = canvas
			L.button = Button
			L.button = Button(window, width="2", height="1", command=store, text="Save")
			L.button.place(x=200, y=0)

	class ReturnC:
		def __init__(HC, canvas, Button):
			HC.canvas = canvas
			HC.button = Button
			HC.button = Button(window, width="2", height="1", command=mainC, text="Quit")
			HC.button.place(x=300, y=0)

	class ChangeB:
		def __init__(C, canvas, Button):
			C.canvas = canvas
			C.button = Button
			C.button = Button(window, width="2", height="1", command=Change, text="B")
			C.button.place(x=400, y=0)

	def resume():
		ball.run = 1
	def Stop():
		ball.run = 0
	def store():
		window = Tk()
		window.title("Name")
		window.geometry('400x300')
		def printValue():
			global text
			pname = player_name.get()
			text = f'{pname}'
		player_name = Entry(window)
		player_name.pack(pady=30)
		Button(window, text="Register Player",padx=10, pady=5,command=printValue).pack()
		window.mainloop()
		print(text)
		f = open("testing.txt", "w")
		f.write(str(text) + " " + str(Score1L) + " " + "\n" + str(posB[0]) + " " + str(posB[1]) + " " + str(posB[2]) + " " + str(posB[3]) + "\n" + str(bar2pos[0]) + " " + str(bar2pos[1]) + " " + str(bar2pos[2]) + " " + str(bar2pos[3]) + "\n" + str(bar1pos[0]) + " " + str(bar1pos[1]) + " " + str(bar1pos[2]) + " " + str(bar1pos[3]))
		f.close()
		f = open("Leader1.txt", "r")
		content = f.read()
		print(content)
		f = open("dummy.txt", "w")
		f.write(str(text) + " " + str(Score1L) + " " + "\n" + content)
		f.close()
		os.remove("Leader1.txt")
		os.rename("dummy.txt", "Leader1.txt")
	def mainC():
		window.destroy()

	def Change():   
		window = Tk()
		window.title("Home")
		canvas = Canvas(window, width=1280, height=720, bg="black")
		canvas.pack()


	window = Tk()
	window.title("Ping Pong1")
	width = 1280
	height= 720
	canvas = Canvas(window, width=1280, height=720, bg="white")
	canvas.pack()
	label = canvas.create_text(640, 20, font = ("Purisa", 30), text="Score: 0")
	window.update()
	bar11 = Bar1(canvas)
	bar22 = Bar2(canvas)
	ball = Ball(canvas, bar11, bar22)
	Pause = PButton(canvas, Button)
	Resume = RButton(canvas, Button)
	DataO = Load(canvas, Button)
	HomeC = ReturnC(canvas, Button)
	HomeB = ChangeB(canvas, Button)
	while True:
		if ball.run == 1:
			bar11.move_bar1()
			bar22.move_bar2()
			ball.bounce()
			ball.Amove_bar2(posB)
			canvas.itemconfig(label, text="Score: "+ str(Score1L))
			window.update_idletasks()
			window.update()
		elif ball.run == 0:
			window.update_idletasks()
			window.update()
	window.update()

window = Tk()
window.title("menu")
window.geometry("1280x720")
canvas = Canvas(window, width=1280, height=720, bg="black")
canvas.pack()
T = canvas.create_text(640, 100, font = ("Purisa", 30), text= "Ping Pong")
OB = PhotoImage(file="1b.png")
OW = PhotoImage(file="1w.png")
SavOB = PhotoImage(file="Saved1b.png")
SavOW = PhotoImage(file="Saved1w.png")
Lead = PhotoImage(file="L.png")
quit = PhotoImage(file="Q.png")
level1w()
level1b()
level1Lw()
level1Lb()
leaderborad()
Quit()
window.mainloop()
