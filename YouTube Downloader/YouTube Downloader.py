# import 라이브러리
from tkinter import *
from pytube import YouTube

# window 생성
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube video downloader")

# 프로그램 상단 라벨 생성
Label(root, text="Youtube Video Downloader", font='arial 20 bold').pack()

# 입력창 생성
link = StringVar()

# 입력창 라벨 생성
Label(root, text="Paste Link Here:", font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)

# 다운로드 함수 생성
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)

# 다운로드 버튼 생성
Button(root,text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx= 2, command=Downloader).place(x=180, y=150)

# 프로그램 실행
root.mainloop()