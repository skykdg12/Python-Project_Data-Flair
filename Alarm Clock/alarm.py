from tkinter import *
import datetime
import time
import winsound  # 기본 사운드

# alarm 함수 생성
def alarm(set_alarm_timer):
    while True:  # 원하는 시간에 도달할 때까지 while문 반복
        time.sleep(1)
        current_time = datetime.datetime.now()  # 현재시간 가져옴
        now = current_time.strftime("%H:%M:%S")  # strftime을 사용해서 문자열 변환
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

# 알람 시간 설정 함수 생성
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}" # f를 통해서 문자열 변환
    alarm(set_alarm_timer)

# 프로그램 양식
clock = Tk() # Tk 실행
clock.title("DataFlair Alarm Clock") # 이름
clock.geometry("400x200") # 크기
time_format = Label(clock, text="Enter time in 24 hour format!",
                    fg="red", bg="black", font="Arial").place(x=60, y=120)
addtime = Label(clock, text="Hour Min sec", font=60).place(x=110)
setYourAlarm = Label(clock, text="When to wake you up", fg="blue",
                     relief="solid", font=("Helevetica", 7, "bold")).place(x=0, y=29)

# 문자값 변환
hour = StringVar()
min = StringVar()
sec = StringVar()

# 알람시간 입력 칸 생성
hourTime = Entry(clock, textvariable=hour, bg="pink",
                 width=15).place(x=110, y=30)
minTime = Entry(clock, textvariable=min, bg="pink",
                width=15).place(x=150, y=30)
secTime = Entry(clock, textvariable=sec, bg="pink",
                width=15).place(x=200, y=30)

# 실행 버튼 생성
submit = Button(clock, text="Set Alarm", fg="red", width=10,
                command = actual_time).place(x=110, y=70)

clock.mainloop()
