from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar, DateEntry


import requests
from bs4 import BeautifulSoup
import time

def main():
    root = Tk()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}


    def work(url):
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        html = response.text
        soup = BeautifulSoup(html, 'lxml')

        result = soup.find('p', class_='p-3')

        if result != NONE:
            result_suc = result.text
            full_result = result_suc.lstrip('\n\t\t\t')
            answer = mb.askyesno(
                title=time.strftime("%c"),
                message=full_result)






    def oven():
        url = 'https://astroscope.ru/horoskop/ejednevniy_goroskop/aries.html'
        work(url)

    def telec():
        url = 'https://astroscope.ru/horoskop/ejednevniy_goroskop/taurus.html'
        work(url)

    def twins():
        url = 'https://astroscope.ru/horoskop/ejednevniy_goroskop/gemini.html'
        work(url)

    def rak():
        url = 'https://astroscope.ru/horoskop/ejednevniy_goroskop/cancer.html'
        work(url)

    def lion():
        url = 'https://astroscope.ru/horoskop/ejednevniy_goroskop/leo.html'
        work(url)

    def deva():
        url = 'https://astroscope.ru/horoskop/ejednevniy_goroskop/virgo.html'
        work(url)

    def vesi():
        url = 'https://astroscope.ru/horoskop/ejednevniy_goroskop/libra.html'
        work(url)

    def scorpioin():
        url = 'https://astroscope.ru/horoskop/ejednevniy_goroskop/scorpio.html'
        work(url)

    def strelec():
        url = 'https://astroscope.ru/horoskop/ejednevniy_goroskop/sagittarius.html'
        work(url)

    def kozerog():
        url = 'https://astroscope.ru/horoskop/ejednevniy_goroskop/capricorn.html'
        work(url)

    def vodolei():
        url = 'https://astroscope.ru/horoskop/ejednevniy_goroskop/aquarius.html'
        work(url)

    def fish():
        url = 'https://astroscope.ru/horoskop/ejednevniy_goroskop/pisces.html'
        work(url)



    def choose_date():
        top = tk.Toplevel(root)
        top.geometry('200x150')

        ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

        def exit_btn():
            top.destroy()
        cal = DateEntry(top, width=12, background='darkblue',
                        foreground='white', borderwidth=2)
        cal.pack(padx=10, pady=10)
        but1 = Button(top, text="Выбрать", command=exit_btn).pack()




    def gor1():
        znak = ent2.get()
        if znak == 'Овен' or znak == 'овен':
            oven()
        if znak == 'Телец' or znak == 'телец':
            telec()
        if znak == 'Близнецы' or znak == 'близнецы':
            twins()
        if znak == 'Рак' or znak == 'рак':
            rak()
        if znak == 'Лев' or znak == 'лев':
            lion()
        if znak == 'Дева' or znak == 'дева':
            deva()
        if znak == 'Весы' or znak == 'весы':
            vesi()
        if znak == 'Скорпион' or znak == 'скорпион':
            scorpioin()
        if znak == 'Стрелец' or znak == 'стрелец':
            strelec()
        if znak == 'Козерог' or znak == 'козерог':
            kozerog()
        if znak == 'Водолей' or znak == 'водолей':
            vodolei()
        if znak == 'Рыбы' or znak == 'рыбы':
            fish()
        if znak == "":
            ans = mb.showerror(
                title='Ошибочка вышла ;)',
                message='Вы неправильно ввели данные ;)'
            )




    root.geometry('350x250')
    root.title('Project by R1T1CK')



    lbl1 = Label(root,text='Выберите дашу вашего рождения', font=24)
    lbl1.place(x = 50, y = 30)

    btn1 = Button(root, text="Выбрать дату", command=choose_date, width=30)
    btn1.place(x=60, y=70)


    lbl1 = Label(root, text='Кто вы по гороскопу?', font=24)
    lbl1.place(x=100, y=100)

    ent2 = Entry(root, width=30)
    ent2.place(x=80, y=130)

    btn2 = Button(root, text="Показать гороскоп", command=gor1, width=30)
    btn2.place(x = 60, y = 160)


    root.mainloop()

if __name__ == "__main__":
    main()