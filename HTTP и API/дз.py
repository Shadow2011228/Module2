import requests


url = 'https://catfact.ninja/fact' # Переменная с ссылкой на API

# GET-запрос
response = requests.get(url)  # делаем запрос по ссылке и получаем ответ в переменную response
print(response.status_code) # Код ответа (200 - успех)
print(response.text) # Выводим текст ответа

data = response.json() # Преобразуем ответ в список со словарями
print(data)
#print('Первый элемент:', data[0])