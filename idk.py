import turtle
t = turtle.Pen()
turtle.bgcolor("black")
yn = turtle.textinput("Enter ya name", "What is ya name")
colors = ["red", "yellow", "blue", "green", "purple", "orange", "white", "teal"]
for x in range(100):
	t.pencolor(colors[x%8])
	t.penup()
	t.forward(x*4)
	t.forward(x*4)
	t.write(yn, font = ("Arial", int( (x + 4) / 4), "bold") )
	t.left(92)
