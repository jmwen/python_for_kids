from tkinter import *
window = Tk()
window.title("Calculator")

expression = ''
equation = StringVar()

def number_clicked(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
def equal():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("error")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
Button(window, text="+",command=lambda:number_clicked("+"),height=1, width=7).grid(row=2,column=3)
Button(window, text="-",command=lambda:number_clicked("-"),height=1, width=7).grid(row=3,column=3)
Button(window, text="*",command=lambda:number_clicked("*"),height=1, width=7).grid(row=4,column=3)
Button(window, text="/",command=lambda:number_clicked("/"),height=1, width=7).grid(row=5,column=3)
Button(window, text=".",command=lambda:number_clicked("."),height=1, width=7).grid(row=5,column=0)
Button(window, text="0",command=lambda:number_clicked("0"),height=1, width=7).grid(row=5,column=1)
Button(window, text="=",command=equal,height=1, width=7).grid(row=5,column=2)
Button(window, text="1",command=lambda:number_clicked("1"),height=1, width=7).grid(row=4,column=0)
Button(window, text="2",command=lambda:number_clicked("2"),height=1, width=7).grid(row=4,column=1)
Button(window, text="3",command=lambda:number_clicked("3"),height=1, width=7).grid(row=4,column=2)
Button(window, text="4",command=lambda:number_clicked("4"),height=1, width=7).grid(row=3,column=0)
Button(window, text="5",command=lambda:number_clicked("5"),height=1, width=7).grid(row=3,column=1)
Button(window, text="6",command=lambda:number_clicked("6"),height=1, width=7).grid(row=3,column=2)
Button(window, text="7",command=lambda:number_clicked("7"),height=1, width=7).grid(row=2,column=0)
Button(window, text="8",command=lambda:number_clicked("8"),height=1, width=7).grid(row=2,column=1)
Button(window, text="9",command=lambda:number_clicked("9"),height=1, width=7).grid(row=2,column=2)
Button(window, text="Clear",command=clear,height=1, width=7).grid(row=1,column=3)

Entry(window, textvariable=equation).grid(columnspan=3, ipadx=25, row=1)
window.mainloop()