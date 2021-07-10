from tkinter import *
import random

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock Paper Scissors')
root.config(bg='seashell3')

Label(root, text='Rock, Paper, Scissors', font='arial 20 bold', bg='seashell2').pack()

# 유저 선택
user_take = StringVar() # 문자열로 변환
Label(root, text='choose any one: rock , paper, scissors', font='arial 15 bold', bg='seashell2').place(x=20, y=70)
Entry(root, font= 'arial 15', textvariable= user_take, bg='antiquewhite2').place(x=90, y=130)

# 컴퓨터 선택
com_pick = random.randint(1, 3)
if com_pick == 1:
    com_pick = 'rock'
elif com_pick == 2:
    com_pick = 'paper'
else:
    com_pick = 'scissors'
    
Result = StringVar()

def play(): # 플레이 함수 생성
    user_pick = user_take.get()
    if user_pick == com_pick:
        Result.set('tie, you both select same')
    elif user_pick == 'rock' and com_pick == 'paper':
        Result.set('you loose, computer select paper')
    elif user_pick == 'paper' and com_pick == 'scissors':
        Result.set('you loose, computer select scissors')
    elif user_pick == 'scissors' and com_pick == 'rock':
        Result.set('you loose, computer select rock')
    elif user_pick == 'rock' and com_pick == 'scissors':
        Result.set('you win, computer select scissors')
    elif user_pick == 'scissors' and com_pick == 'paper':
        Result.set('you win, computer select paper')
    elif user_pick == 'paper' and com_pick == 'rock':
        Result.set('you win, computer select rock')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')

def Reset(): 
    Result.set("")
    user_take.set("")
    
def Exit():
    root.destroy()
    
Entry(root, font='arial 10 bold', textvariable= Result, bg='antiquewhite2', width = 50).place(x=25, y=250)

Button(root, font = 'arial 13 bold', text='PLAY', padx=5, bg='seashell4', command=play).place(x=150, y=190)

Button(root, font = 'arial 13 bold', text='RESET', padx=5, bg='seashell4', command=Reset).place(x=70, y=310)

Button(root, font = 'arial 13 bold', text='EXIT', padx=5, bg='seashell4', command=Exit).place(x=230, y=310)

root.mainloop()