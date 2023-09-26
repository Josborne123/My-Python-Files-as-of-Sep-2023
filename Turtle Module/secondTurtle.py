import turtle
import random


john = turtle.Turtle()
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']


# Set colors for turtle
john.color('red', 'blue')


# Set pen width 
john.width(5)


# Fill in shape with color
john.begin_fill()
john.circle(50)
john.end_fill()


john.penup()
john.forward(150)
john.pendown()

john.color('yellow', 'cyan')


john.begin_fill()
for x in range(4):
	john.forward(100)
	john.right(90)
john.end_fill()

for x in range(5):
	randColor = random.randrange(0, len(colors))
	john.color(colors[randColor])
	rand1 = random.randrange(-300, 300)
	rand2 = random.randrange(-300, 300)
	john.penup()
	john.setpos(rand1, rand2)
	john.pendown()
	john.begin_fill()
	john.circle(random.randrange(0, 80))
	john.end_fill








turtle.done()