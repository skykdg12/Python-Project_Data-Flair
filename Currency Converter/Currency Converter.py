# Python Project on Currency Converter

# import 라이브러리
import requests # to get url
from tkinter import *
import tkinter as tk
from tkinter import ttk

# 실시간 환율 변환 클래스 생성
class RealTimeCurrencyConverter():
    def __init__(self,url):
        # requests로 url을 파이썬으로 로드, json이 페이지를 json파일로 변환해서 data에 저장
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']

# 환율 변환 함수 생성, 환전 전, 환전 후, 환전량
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'KRW':
            amount = amount / self.currencies[from_currency]

        # 소수점 4자리까지 표시    
        amount = round(amount * self.currencies[to_currency], 4)
        return amount


class App(tk.Tk):

    # 프레임 생성
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = 'Currency Converter'
        self.currency_converter = converter

        # converter 생성
        self.geometry("500x200")

        # Label
        self.intro_label = Label(self, text='Welcome to Real Time Currency Convertor', fg='blue', relief=tk.RAISED, borderwidth=3)
        self.intro_label.config(font=('Courier', 15, 'bold'))

        self.date_label = Label(self, text=f"1 Indian Rupee equals={self.currency_converter.convert('INR', 'USD', 1)}USD \n Date: {self.currency_converter.data['date']}", relief=tk.GROOVE, borderwidth=5)
       
        self.intro_label.place(x=10, y=5)
        self.date_label.place(x=170, y=50)

        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')  # restricNumberOnly 함수로 사용자가 Amount 필드에 잘못된 번호 입력 하는것을 제한함
        self.amount_field = Entry(self, bd = 3, relief=tk.RIDGE, justify = tk.CENTER, validate = 'key', validatecommand = valid)
        self.converted_amount_field_label = Label(self, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 3)
        

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("USD")
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("KRW")

        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable, values=list(self.currency_converter.currencies.keys()), font=font, state='readonly', width=12, justify=tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable, values=list(self.currency_converter.currencies.keys()), font=font, state='readonly', width=12, justify=tk.CENTER)

        # placing
        self.from_currency_dropdown.place(x=30, y=120)
        self.amount_field.place(x=36, y=150)
        self.to_currency_dropdown.place(x=340, y=120)
        self.converted_amount_field_label.place(x=346, y=150)

        # Convert button
        self.convert_button = Button(self, text='Convert', fg="black", command=self.perform)
        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.convert_button.place(x=225, y=135)

    # 유저가 입력한 값을 원하는 통화로 변환해서 converted_amount 값에 입력
    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount, 2)

        self.converted_amount_field_label.config(text = str(converted_amount))

    # 금액필드에 숫자만 입력하도록 함수 생성
    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))

# 실행
if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)

    App(converter)
    mainloop()

