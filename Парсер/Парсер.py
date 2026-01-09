import time

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from tkinter import *
import math


class Weather:
    def __init__(self, link='https://rp5.ru/Погода_в_России'):
        self.link = link
        data = []
        r = ''
        while r == '' or 'Обнаружена блокировка рекламы' in r: # Если r пустая, то повторить код
            r = requests.get(self.link, headers={'User-Agent': UserAgent().chrome}).text # Берем весь html код по ссылке
            print('Нашел:', r)

            self.soup = BeautifulSoup(r, 'html.parser') # Преобразуем в удобный формат html-парсера




    def first_parse(self):
        # Ищем в html коде тег div, где class=Rulinks, получаем список с городами в теге <a>
        data = self.soup.find_all("div", {'class': 'RuLinks'})

        links = {}
        for tag in data: # пробегаемся по списку и формируем словарь, где ключ=названию города, а значение = ссылка на его погоду
            print(tag)
            if tag.find_next("b"):
                tag = tag.find_next("a") # ищем тег <a>
                links[tag.get_text()] = "https://rp5.ru/" + tag['href'] # формируем словарь
        return links

    def parse_next(self, link):
        soup = Weather(link).soup
        # Надо попытаться найти погоду
        if soup.find('div', {'id': 'archiveString'}):
            data = soup.find('div', {'id': 'archiveString'})
            temp = data.find_next("span", {'class': 't_0'}).get_text()
            return temp
        # Погоды нет
        print(soup.text)
        try:
            data = soup.find("div", {"class": "countryMap"})
            data = data.find_all("a")
            links = {}
            for tag in data:
                links[tag.get_text()] = "https://rp5.ru/" + tag['href']

        except:
            return self.parse_next(link)

        return links



class UI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Погода")

        self.upper_frame = Frame(self.root)
        self.upper_frame.grid(row=0, column=0)

        self.w = Weather()
        one = {}
        while one == {}:
            print('Ищу 1')
            time.sleep(0.1)
            one = self.w.first_parse()

        self.set_buttons(one)

        self.lower_frame = Frame(self.root)
        self.lower_frame.grid(row=1, column=0)

        self.home_btn = Button(self.lower_frame, text="Домой", fg="red", font=("Algerian", 23),
                               command=self.home_button_handler)
        self.home_btn.pack()
    def home_button_handler(self):
        self.upper_frame.destroy()
        self.upper_frame = Frame(self.root)
        self.upper_frame.grid(row=0, column=0)

        self.w = Weather()
        one = self.w.first_parse()
        self.set_buttons(one)
    def run(self):
        self.root.mainloop()

    def button_handler(self, c): # Метод который вызывается при нажатии на кнопку города
        self.upper_frame.destroy()
        self.upper_frame = Frame(self.root)
        self.upper_frame.grid(row=0, column=0)
        two = {}
        while two == {}:
            print('Ищу 2')
            two = self.w.parse_next(c) # Ищет погоду в выбранном городе или возвращает города региона
        if isinstance(two, dict): # Проверяем является ли two словарем
            self.set_buttons(two)
        else:
            label = Label(self.upper_frame, text=two, font=(None, 22))
            label.pack()

        self.root.update_idletasks()
    def set_buttons(self, links):
        total_links = len(links) # Узнаем длину словаря с городами
        columns = math.ceil(total_links / 22)  # Вычисляем кол-во столбцов в окне

        for i, (name, link) in enumerate(links.items()):  # Пробегаемся по словарю с городами
            row = i // columns # Вычисляем строку на сетке
            col = i % columns # Вычисляем столбец на сетке
            button = Button(self.upper_frame, text=name, command=lambda c=link: self.button_handler(c)) # Создаем кнопку для города
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew") # Размещаем кнопку на окне

if __name__ == '__main__':
    root = UI()

    root.run()