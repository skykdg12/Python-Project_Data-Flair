# 라이브러리
from tkinter import *

# 윈도우 창 생성
root = Tk()
root.geometry('400x400')
root.config(bg='SlateGray3')
root.resizable(0,0)
root.title('Address Book')

# 연락처 정보
contactlist = [
    ['Parv Maheswari', '0176738493'],
    ['David sharma', '2684430000'],
    ['Mandish Kabra', '4338354432'],
    ['Prisha Modi', '6834552341'],
    ['Rahul kaushik', '1234852689'],
    ['Johena Shaa', '2119876543'],
]

# 변수 값 지정
Name = StringVar()
Number = StringVar()

# 연락처 담을 프레임 생성
frame = Frame(root)
frame.pack(side=RIGHT)

# 프레임에 스크롤 생성
scroll = Scrollbar(frame, orient=VERTICAL) # 프레임 우측에 수직 스크롤 생성
select = Listbox(frame, yscrollcommand=scroll.set, height=12) # 프레임 안에 있는 연락처 선택 한 화면에 12개까지 표시
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y) # 스크롤 위치 지정
select.pack(side=LEFT, fill=BOTH, expand=1) # 선택할 주소들 위치 지정

# 함수 생성
def Selected(): # 선택된 값 반환
    return int(select.curselection()[0])

def AddContact(): # 새 연락처 추가
    contactlist.append([Name.get(), Number.get()])
    Select_set()

def EDIT(): # 기존 연락처 편집
    contactlist[Selected()] = [Name.get(), Number.get()]
    Select_set()

def DELETE(): # 선택 연락처 삭제
    del contactlist[Selected()]
    Select_set()

def VIEW(): # 선택 연락처 보기
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)

def EXIT():
    root.destroy()

def RESET():
    Name.set('')
    Number.set('')

def Select_set(): # 연락처 관리
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)
Select_set()

# 버튼 및 라벨 생성
Label(root, text='NAME', font='arial 12 bold', bg='SlateGray3').place(x=30, y=20)
Entry(root, textvariable=Name).place(x=100, y=20)

Label(root, text='PHONE NO.', font='arial 12 bold', bg='SlateGray3').place(x=30, y=70)
Entry(root, textvariable=Number).place(x=130, y=70)

Button(root, text='ADD', font='arial 12 bold', bg='SlateGray4', command=AddContact).place(x=50, y=110)
Button(root, text="EDIT", font='arial 12 bold', bg='SlateGray4', command=EDIT).place(x=50, y=260)
Button(root, text="DELETE", font='arial 12 bold', bg='SlateGray4', command=DELETE).place(x=50, y=210)
Button(root, text="VIEW", font='arial 12 bold', bg='SlateGray4', command=VIEW).place(x=50, y=160)
Button(root, text="EXIT", font='arial 12 bold', bg='tomato', command=EXIT).place(x=300, y=320)
Button(root, text="RESET", font='arial 12 bold', bg='SlateGray4', command=RESET).place(x=50, y=310)

# 실행
root.mainloop()