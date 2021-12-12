import turtle
from turtle import *
screensize(canvwidth=400, canvheight=400, bg='black')
width(5)

#
# Drawing 'Happy'
#

# Drawing 'H'
pencolor('red')
up()
goto(x= -200, y= 55)
left(90)
down()
forward(100)
backward(50)
right(90)
forward(50)
left(90)
forward(50)
backward(100)

# Drawing 'a'
up()
right(90)
goto(x= -115, y= 55)
down()
circle(25)
up()
goto(x= -90, y= 105)
down()
right(90)
forward(50)

# Drwaing 'p'
for i in (1, 2):
    pencolor('orange')
    up()
    left(90)
    forward(10)
    left(90)
    forward(50)
    right(180)
    down()
    forward(75)
    up()
    right(180)
    forward(25)
    right(90)
    forward(25)
    down()
    circle(25)
    up()
    forward(25)
    right(90)

# Drawing 'y'
pencolor('yellow')
goto(x= 40, y= 105)
down()
goto(x= 65, y= 55)
up()
goto(x= 90, y= 105)
down()
goto(x= 52, y= 30)

#
# Completed 'Happy'
#

#
# Drawing 'Father's'
#

# Drawing 'F'
pencolor('green yellow')
up()
goto(x= -300, y= -20)
down()
left(90)
forward(50)
backward(50)
right(90)
forward(100)
backward(50)
left(90)
forward(50)

# Drawing 'a'
pencolor('forest green')
up()
goto(x= -215, y= -120)
down()
circle(25)
up()
forward(25)
down()
left(90)
forward(50) 

# Drawing 't'
up()
right(90)
forward(10)
down()
forward(50)
backward(25)
left(90)
forward(50)
backward(90)
goto(-130, -120)

# Drawing 'h'
pencolor('light sea green')
up()
goto(-110, -120)
down()
# left(90)
forward(100)
backward(50)
right(90)
forward(50)
right(90)
forward(50)

# Drawing 'e'
up()
goto(-25, -120)
down()
left(90)
circle(25)
up()
goto(-50, -95)
down()
forward(50)
up()
right(90)
forward(10)
pencolor('black')
width(10)
down()
right(90)
forward(25)
width(5)

# Drawing 'r'
pencolor('royal blue')
up()
goto(10, -120)
# up()
# forward(10000000000000000000000000000000000000000000000)