import turtle
import time
import random

screen = turtle.Screen()
screen.bgcolor('black')
screen.title('Snake Game')
screen.setup(width=500, height=500)
screen.tracer(0)

snake = []                          # This list stores all the turtles that create each snake part.
score = 0                           # This is the score.
size = 20                           # The size of the apple and the snake.
key = ''                            # This is going to store which key and direction.

def key_up():
    global key
    if key != 'down':
        key = 'up'
def key_down():
    global key
    if key != 'up':
        key = 'down'
def key_left():
    global key
    if key != 'right':
        key = 'left'
def key_right():
    global key
    if key != 'left':
        key = 'right'

def move_head():
    if key == 'up':
        head.sety(head.ycor() + size)
    if key == 'down':
        head.sety(head.ycor() - size)
    if key == 'left':
        head.setx(head.xcor() - size)
    if key == 'right':
        head.setx(head.xcor() + size)

def draw_apple():
    applex = random.randint(-11,11)*20
    appley = random.randint(-11,11)*20
    apple.goto(applex,appley)

def draw_snake():
    snake_body = turtle.Turtle()
    snake_body.speed(0)
    snake_body.shape('square')
    snake_body.color('Green')
    snake_body.penup()
    snake_body.goto(0, 0)
    snake.append(snake_body)

def change_score(s):
    score_turtle.goto(100,210)
    score_turtle.clear()
    string = 'Score: {}'.format(score)
    score_turtle.write(string,font=('Arial',20,'bold'))
    score_turtle.hideturtle()

def move_body():
    positions = []
    for i in snake:
        x = i.xcor()
        y = i.ycor()
        positions.append({'x': x, 'y': y})
    for i in range(1,len(snake)):
        snake[i].goto(positions[i-1]['x'],positions[i-1]['y'])

def check_collision():
    global key
    collision = False
    if head.xcor() < -240 or head.xcor() > 240 or head.ycor() < -240 or head.ycor() > 240:
        collision = True
    for i in range(1,len(snake)):
        if head.xcor() == snake[i].xcor() and head.ycor() == snake[i].ycor():
            collision = True
    if collision == True:
        key = ''
        time.sleep(1)
        for s in snake:
            s.goto(20000000000,200000000)
        apple.goto(25000000000,250000000)
        over = turtle.Turtle()
        over.speed(0)
        over.penup()
        over.goto(-170,0)
        over.color('White')
        over.write('GAME OVER!',font=('Arial',40,'bold'))
        over.hideturtle
        print(apple.xcor())
    return collision

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('Green')
head.penup()
head.goto(0, 0)
snake.append(head)

apple = turtle.Turtle()
apple.speed(0)
apple.shape('square')
apple.color('Red')
apple.penup()
draw_apple()

score_turtle = turtle.Turtle()
score_turtle.speed(0)
score_turtle.color('White')
score_turtle.penup()
change_score(0)

screen.listen()
screen.onkeypress(key_up, 'Up')
screen.onkeypress(key_down, 'Down')
screen.onkeypress(key_left, 'Left')
screen.onkeypress(key_right, 'Right')

while True:
    screen.update()
    if head.distance(apple) <=0:
        draw_apple()
        draw_snake()
        score+=1
        change_score(score)
    move_body()
    move_head()
    if check_collision():
        break
    time.sleep(0.15)

screen.mainloop()