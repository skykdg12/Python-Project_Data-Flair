# 라이브러리
from tkinter import *
import base64  # 이진수 데이터를 ASCII문자로 인코딩하고 다시 이진수 데이터로 디코딩하는 기능 제공

# 프로그램 창 생성
root = Tk()
root.geometry('500x300')
root.resizable(0, 0)  # 창의 고정 크기 설정
root.title("Message Encode and Decode")

# 프로그램 제목
Label(root, text='ENCODE DECODE', font='arial 20 bold').pack()

# 입력할 변수 값 지정
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

# Encode 함수 생성
def Encode(key, message):
    enc = []

    for i in range(len(message)):  # 메세지 길이까지 루프 실행
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256)) # ord() 문자열을 받아서 정수 값으로 반환, chr() 함수는 정수 값을 받아 문자열로 반환
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
    # base64.urlsafe_b64encode은 문자열 인코딩, join()으로 문자열, 튜플의 각 요소 결합하고 연결된 문자열 반환
    # encode() 문자열의 utf-8 인코딩 메세지 반환
    # decode() 문자열 디코딩

# Decode 함수 생성
def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()  # 입력한 메세지를 디코드해서 결과값으로 반환

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)

# Mode 함수 생성
def Mode():
    if (mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))# private_key.get(), Text.get() 값은 Encode()와 Decode() 함수의 인수에 전달
    elif (mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

# 종료 함수 생성
def Exit():
    root.destroy()

# 리셋 함수 생성
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


# 라벨 및 버튼 생성
Label(root, font='arial 12 bold', text='MESSAGE').place(x=60, y=60)
Entry(root, font='arial 10', textvariable=Text,bg='ghost white').place(x=290, y=60)

Label(root, font='airal 12 bold', text='KEY').place(x=60, y=90)
Entry(root, font='arial 10', textvariable=private_key,bg='ghost white').place(x=290, y=90)

Label(root, font='arial 12 bold',text='MODE(e-encode, d-decode)').place(x=60, y=120)
Entry(root, font='arial 10', textvariable=mode,bg='ghost white').place(x=290, y=120)
Entry(root, font='arial 10 bold', textvariable=Result,bg='ghost white').place(x=290, y=150)

Button(root, font='arial 10 bold', text='RESULT', padx=2,bg='LightGray', command=Mode).place(x=60, y=150)
Button(root, font='arial 10 bold', text='RESET', width=6,command=Reset, bg='LimeGreen', padx=2).place(x=80, y=190)
Button(root, font='arial 10 bold', text='EXIT', width=6, command=Exit,bg='OrangeRed', padx=2, pady=2).place(x=180, y=190)

# 실행
root.mainloop()