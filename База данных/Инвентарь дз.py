import  s_taper
from s_taper.consts import *
import random


scheme = {
    'user_id': INT + KEY,
    'inv': TEXT,
}

inventar = s_taper.Taper('inventar', 'data.db').create_table(scheme)

user1_list = [101, {"Топор":2}] # Создаем список с записью в таблицу (кол-во элементов = столбцов)
inventar.write(user1_list) # используем метод write передавая 1 аргумент список, который хотим положить в таблицу

user1_list = [99, {"Кирка":3}] # Создаем список с записью в таблицу (кол-во элементов = столбцов)
inventar.write(user1_list) # используем метод write передавая 1 аргумент список, который хотим положить в таблицу


user_list = inventar.read('user_id', 101) # Берем из таблицы запись
print(user_list[1]) # Выводим в консоль словарь
print(user_list[1]['Топор']) # Выводим в консоль значение из словаря
user_list[1]['Топор']+=1 # Прибавляем к значению 1-у
print(user_list) # Проверяем себя

inventar.write(user_list) # Записываем измененную запись в таблицу
user_list = inventar.read('user_id', 101) # Снова берем из таблицы запись
print(user_list) # Проверяем себя

def inv(id):
    user_list = inventar.read('user_id', id)  # Берем из таблицы запись
    print(user_list[1])  # Выводим в консоль словарь

inv(99)

def a(id, key, value):
    user_list = inventar.read('user_id', id)  # Берем из таблицы запись
    user_list[1][key]=value
    inventar.write(user_list)  # Записываем измененную запись в таблицу
a(99,'Лопата',5)
a(99,'Стрела',3)
a(99,'винтовка',15)
a(99,'Граната',6)

inv(99)
names=["Лук", 'Щит', 'Броня', 'Мотыга', 'Стейк', 'Ведро']
for i in range(1000):
    r=random.choice(names)
    b=random.randint(1,32)
    a(99, r, b)
    inv(99)