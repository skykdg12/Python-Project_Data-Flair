import tkinter # Tkinter는 Tcl/Tk에 대한 파이썬 Wrapper로서 Tcl/Tk를 파이썬에 사용할 수 있도록 한 Lightweight GUI 모듈이다
from PIL import Image, ImageTk # Tcl은 Tool Command Language의 약자로서 일종의 프로그래밍 언어이며, Tk는 크로스 플랫폼에 사용되는 일종의 GUI 툴킷이다.
import random # 무작위로 주사위를 굴리기 위함

# 프로그램의 가장 상단에 위치
root = tkinter.Tk() # Tk 클래스 객체(root)를 생성
root.geometry('400x400') # 프로그램 크기
root.title('DataFlair Roll the Dice') # 프로그램의 이름

# 프레임 안에 라벨 삽입
l0 = tkinter.Label(root, text="")

# 위젯의 위치를 정하는 방법으로 위젯들을 부모 위젯에 모두 패킹하여 불필요한 공간을 없앤다 위젯.pack() 메서드를 사용한다
l0.pack() 
l1 = tkinter.Label(root, text="Hello from DataFlair!", fg = "light green", # 프로그램 제목과 글꼴 색 등
                             bg = "dark green", font = "Helvetica 16 bold italic")
l1.pack()

# 이미지 생성
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

# 이미지들을 랜덤으로 선택
diceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# 주사위 이미지 라벨 생성
ImageLabel = tkinter.Label(root, image=diceImage)
ImageLabel.image = diceImage

# 위젯을 부모 위젯에 패킹
ImageLabel.pack(expand=True)

# 버튼 기능 생성
def rolling_dice():
    diceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # 이미지 업데이트
    ImageLabel.configure(image=diceImage)
    # 이미지 참조
    ImageLabel.image = diceImage

# 버튼을 생성해서 이름과 기능 추가
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)

# 위젯을 부모위젯에 패킹
button.pack(expand=True)

root.mainloop() # mainloop()는 이벤트 메시지 루프로서 키보드나 마우스 혹은 화면 Redraw와 같은 다양한 이벤트로부터 오는 메시지를 받고 전달하는 역활을 한다