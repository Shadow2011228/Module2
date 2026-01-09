import requests
import json


url = 'https://catfact.ninja/fact' # Переменная с ссылкой на API

list1=[]

for i in range(10):
    response = requests.get(url)  # делаем запрос по ссылке и получаем ответ в переменную response
    print(response.status_code) # Код ответа (200 - успех)
    print(response.text) # Выводим текст ответа

    data = response.json() # Преобразуем ответ в список со словарями
    print(data)

    list1.append(data)

# response = requests.get(url)  # делаем запрос по ссылке и получаем ответ в переменную response
# print(response.status_code) # Код ответа (200 - успех)
# print(response.text) # Выводим текст ответа
#
# data = response.json() # Преобразуем ответ в список со словарями
# print(data)
#
# list1.append(data)
#
# response = requests.get(url)  # делаем запрос по ссылке и получаем ответ в переменную response
# print(response.status_code) # Код ответа (200 - успех)
# print(response.text) # Выводим текст ответа
#
# data = response.json() # Преобразуем ответ в список со словарями
# print(data)
#
# list1.append(data)
#
# response = requests.get(url)  # делаем запрос по ссылке и получаем ответ в переменную response
# print(response.status_code) # Код ответа (200 - успех)
# print(response.text) # Выводим текст ответа
#
# data = response.json() # Преобразуем ответ в список со словарями
# print(data)
#
# list1.append(data)
#
# response = requests.get(url)  # делаем запрос по ссылке и получаем ответ в переменную response
# print(response.status_code) # Код ответа (200 - успех)
# print(response.text) # Выводим текст ответа
#
# data = response.json() # Преобразуем ответ в список со словарями
# print(data)
#
# list1.append(data)
#
# response = requests.get(url)  # делаем запрос по ссылке и получаем ответ в переменную response
# print(response.status_code) # Код ответа (200 - успех)
# print(response.text) # Выводим текст ответа
#
# data = response.json() # Преобразуем ответ в список со словарями
# print(data)
#
# list1.append(data)
#
# response = requests.get(url)  # делаем запрос по ссылке и получаем ответ в переменную response
# print(response.status_code) # Код ответа (200 - успех)
# print(response.text) # Выводим текст ответа
#
# data = response.json() # Преобразуем ответ в список со словарями
# print(data)
#
# list1.append(data)
#
# response = requests.get(url)  # делаем запрос по ссылке и получаем ответ в переменную response
# print(response.status_code) # Код ответа (200 - успех)
# print(response.text) # Выводим текст ответа
#
# data = response.json() # Преобразуем ответ в список со словарями
# print(data)
#
# list1.append(data)
#
# response = requests.get(url)  # делаем запрос по ссылке и получаем ответ в переменную response
# print(response.status_code) # Код ответа (200 - успех)
# print(response.text) # Выводим текст ответа
#
# data = response.json() # Преобразуем ответ в список со словарями
# print(data)
#
# list1.append(data)
#
# response = requests.get(url)  # делаем запрос по ссылке и получаем ответ в переменную response
# print(response.status_code) # Код ответа (200 - успех)
# print(response.text) # Выводим текст ответа
#
# data = response.json() # Преобразуем ответ в список со словарями
# print(data)
#
# list1.append(data)

with open('cats.json', 'w') as file:
    json.dump(list1, file, indent=4)


with open('cats.json', 'r') as file:
    python_dict = json.load(file)
print(python_dict)