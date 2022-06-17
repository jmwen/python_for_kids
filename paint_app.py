from tkinter import *
from tkinter import colorchooser
x, y = 0,0
fill = None
outline = "black"
size_num = 1

screen = Tk()
screen.title("Paint Application")
screen.state("zoomed")
screen.rowconfigure(0, weight = 1)
screen.columnconfigure(0, weight = 1)

canvas = Canvas(screen, background = "white")
canvas.grid(row = 0, column = 0, sticky = "NSEW")

def draw_line(event):
    global x, y, size_num, outline
    canvas.create_line((x, y, event.x, event.y), fill = outline, width = size_num)
    x, y = event.x, event.y

def draw_square(event):
    global x, y, size_num, outline, fill
    canvas.create_rectangle((x, y, event.x, event.y), outline = outline, fill = fill, width = size_num)
    x, y = event.x, event.y

def draw_circle(event):
    global x, y, size_num, outline, fill
    canvas.create_oval((x, y, event.x, event.y), outline = outline, fill = fill, width = size_num)
    x, y=event.x, event.y

def shape(choice):
    if choice == 1:
        canvas.unbind("<ButtonRelease-1>")
        canvas.bind("<B1-Motion>", draw_line)
    elif choice == 2:
        canvas.unbind("<B1-Motion>")
        canvas.bind("<ButtonRelease-1>", draw_line)
    elif choice == 3:
        canvas.unbind("<B1-Motion>")
        canvas.bind("<ButtonRelease-1>", draw_square)
    else:
        canvas.unbind("<B1-Motion>")
        canvas.bind("<ButtonRelease-1>", draw_circle)

def size(choice):
    global size_num
    size_num = choice

def color(choice):
    global outline, fill
    chosen_color = colorchooser.askcolor(title = "Choose Color")
    if choice == 1:
        outline = chosen_color[1]
    elif choice == 2:
        fill = chosen_color[1]
    elif choice == 3:
        canvas["background"] = chosen_color[1]

def clear():
    global outline, fill
    canvas.delete("all")
    canvas["background"] = "white"
    outline = "black"
    fill = None

def position(event):
    global x, y
    x, y = event.x, event.y

canvas.bind("<Button-1>", position)

main = Menu(screen)

shape_menu = Menu(main)
main.add_cascade(label = "Draw Options", menu = shape_menu)
shape_menu.add_command(label="Pen", command=lambda: shape(1))
shape_menu.add_command(label="Line", command=lambda: shape(2))
shape_menu.add_command(label="Square", command=lambda: shape(3))
shape_menu.add_command(label="Circle", command=lambda: shape(4))

size_menu = Menu(main)
main.add_cascade(label="Size", menu=size_menu)
size_menu.add_command(label="1", command=lambda: size(1))
size_menu.add_command(label="5", command=lambda: size(5))
size_menu.add_command(label="10", command=lambda: size(10))
size_menu.add_command(label="15", command=lambda: size(15))
size_menu.add_command(label="20", command=lambda: size(20))
size_menu.add_command(label="25", command=lambda: size(25))
size_menu.add_command(label="30", command=lambda: size(30))

color_menu = Menu(main)
main.add_cascade(label="Color", menu=color_menu)
color_menu.add_command(label="Outline Color", command=lambda: color(1))
color_menu.add_command(label="Fill Color", command=lambda: color(2))
color_menu.add_command(label="Background Color", command=lambda: color(3))

clear_menu = Menu(main)
main.add_cascade(label="Clear", menu=clear_menu)
clear_menu.add_command(label="Clear", command=clear)

screen.config(menu=main)

screen.mainloop()