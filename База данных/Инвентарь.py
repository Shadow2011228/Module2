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

user_list = inventar.read('user_id', 101) # Берем из таблицы запись
print(user_list[1]) # Выводим в консоль словарь
print(user_list[1]['Топор']) # Выводим в консоль значение из словаря
user_list[1]['Топор']+=1 # Прибавляем к значению 1-у
print(user_list) # Проверяем себя

inventar.write(user_list) # Записываем измененную запись в таблицу
user_list = inventar.read('user_id', 101) # Снова берем из таблицы запись
print(user_list) # Проверяем себя