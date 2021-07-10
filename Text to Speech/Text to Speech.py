# Import Libraries
from os import remove
from tkinter import *
from gtts import gTTS
from playsound import playsound

# Initializing window
root = Tk()
root.geometry("350x300")
root.configure(bg='ghost white')
root.title("Text to Speech")

# 프로그램 Head 생성
Label(root, text= "Text to Speech", font="arial 20 bold", bg='white smoke').pack()

# 입력창 라벨 생성
Label(root, text="Enter Text", font='arial 15 bold', bg='white smoke').place(x=20,y=60)

# 문자열로 입력 하도록 변수 생성
Msg = StringVar()

# 입력창 생성 및 위치 지정
entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)

# Convert Function 생성
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text=Message)
    speech.save(f'{Message}.mp3')
    playsound(f'{Message}.mp3')

# 나가기 함수 생성
def Exit():
    root.destroy()

# 리셋 함수 생성
def Reset():
    Msg.set("")
    

# 플레이, 나가기, 리셋 버튼 생성
Button(root, text="PLAY", font= "arial 15 bold", command= Text_to_speech, width='4').place(x=25, y=140)
Button(root, font="arial 15 bold", text="EXIT", width='4', command= Exit, bg="OrangeRed1").place(x=100, y=140)
Button(root, font="arial 15 bold", text="RESET", width='6', command=Reset).place(x=175, y=140)

# 프로그램 실행
root.mainloop()