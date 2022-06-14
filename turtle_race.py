import turtle
from random import *
s = turtle.getscreen()
turtle.hideturtle
class Turtle:
    def __init__(self,color):
        self.turtle =  turtle.Turtle()
        self.turtle.pensize(5)
        self.turtle.shape("turtle")
        self.turtle.up()
        if color.lower() == "red":
            self.turtle.color("Red")
            self.turtle.goto(-250, 150)
        elif color.lower() == "green":
            self.turtle.color("Green")        
            self.turtle.goto(-250,0)
        else:
            self.turtle.color("Blue")
            self.turtle.goto(-250,-150)
        self.turtle.down()
    def move(self):
        self.turtle.forward(randint(1,10))

Red = Turtle("Red")
Green = Turtle("Green")
Blue = Turtle("Blue")
for i in range(1,101):
    Red.move()
    Green.move()
    Blue.move()        