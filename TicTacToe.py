from tkinter import *
from tkinter import messagebox
Game = Tk()
Game.title("Tic Tac Toe")
turn = 0
state = ['','','','','','','','','']
winner = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8],
[0,4,8], [2,4,6]]
game = True

def winnercheck(player):
    global state,winner,game
    for i in winner:
        if((state[i[0]] == player) and (state[i[1]] == player) and (state[i[2]] == player)):
            string = '{} won!'.format(player)
            messagebox.showinfo('showinfo',string)
            game = False

def mark(button,number):
    global turn, state, game
    if button['text'] == ' ' and game == True:
        if turn % 2 == 1:
            button['text'] = 'X'
            turn += 1
            state[number-1] = 'X'
            winnercheck('X')
        elif turn % 2 == 0:
            button['text'] = 'O'
            turn += 1
            state[number-1] = 'O'
            winnercheck('O')
    else:
        if game == False:
            messagebox.showinfo('showinfo','Game over! Start a new game.')
        elif button['text'] != ' ':
            messagebox.showinfo('showinfo','This box is occupied!')
    if turn > 8 and game == True:
        messagebox.showinfo('showinfo','The match was a Draw')
        game = False

font = ('Helvetica',20,'bold')
NW = Button(Game, text=' ', width=4, height=2, font = font,command = lambda: mark(NW,1))
NW.grid(row=0,column=0)
N = Button(Game, text=' ', width=4, height=2, font = font,command = lambda: mark(N,2))
N.grid(row=0,column=1)
NE = Button(Game, text=' ', width=4, height=2, font = font,command = lambda: mark(NE,3))
NE.grid(row=0,column=2)
W = Button(Game, text=' ', width=4, height=2, font = font,command = lambda: mark(W,4))
W.grid(row=1,column=0)
Center = Button(Game, text=' ', width=4, height=2, font=font,command = lambda: mark(Center,5))
Center.grid(row=1, column=1)
E = Button(Game, text=' ', width=4, height=2, font = font,command = lambda: mark(E,6))
E.grid(row=1,column=2)
SW = Button(Game, text=' ', width=4, height=2, font = font,command = lambda: mark(SW,7))
SW.grid(row=2,column=0)
S = Button(Game, text=' ', width=4, height=2, font = font,command = lambda: mark(S,8))
S.grid(row=2,column=1)
SE = Button(Game, text=' ', width=4, height=2, font = font,command = lambda: mark(SE,9))
SE.grid(row=2,column=2)

buttons = [NW, N, NE, W, Center, E, SW, S, SE]

def new_game():
    global state,game,turn,buttons
    turn = 0
    state = ['','','','','','','','','']
    game = True
    for b in buttons:
        b['text'] = ' '

Button(Game, text='New Game', command=new_game).grid(row=3, column=1)

Game.mainloop()
