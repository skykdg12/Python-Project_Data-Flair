# GUI 라이브러리
from tkinter import *

# 랜덤 문자형
import random
import string

# 클립보드에 복사하는 기능
import pyperclip

# 프로그램 메뉴바 생성
root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("PASSWORD GENERATOR")

# 프로그램 전면 제목 생성
Label(root, text="PASSWORD GENERATOR", font='arial 15 bold').pack()

# 패스워드 항목 이름 생성
pass_label = Label(root, text="PASSWORD LENGTH", font='arial 10 bold').pack()

# 정수 자료형 선언
pass_len = IntVar()

# 스핀박스를 통해 8부터 32까지 패스워드 길이 선택
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack()

# 생성된 비밀번호를 저장하는 문자형 변수
pass_str = StringVar()

# Generator 함수 생성


def Generator():
    password = ''

# 대문자, 소문자, 숫자 및 특수 기호 조합인 길이4의 문자열 생성해서 암호 변수에 저장
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(
            string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)

# 사용자가 입력한 임의의 문자열 생성 후 암호 변수에 추가, 위에서 길이 4의 문자열을 이미 생성했기 때문에 -4를 함
    for y in range(pass_len.get() - 4):
        password = password + \
            random.choice(string.ascii_uppercase +
                          string.ascii_lowercase+string.digits+string.punctuation)

# 패스워드 저장
    pass_str.set(password)


# 버튼 생성 및 커맨드 지정
Button(root, text="GENERATE PASSWORD", command=Generator).pack(pady=5)

# 생성한 비밀번호를 엔트리에 입력
Entry(root, textvariable=pass_str).pack()

# 패스워드 복사 함수 생성


def Copy_password():

    # 비밀번호를 클립보드에 복사
    pyperclip.copy(pass_str.get())


# 버튼 생성 및 커맨드 지정
Button(root, text='COPY TO CLIPBOARD', command=Copy_password).pack(pady=5)

# 프로그램 실행
root.mainloop()
