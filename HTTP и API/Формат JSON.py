import json
import requests

json_data = '{"name": "Alice", "age": 25, "skills": ["Python", "API"]}' # Создаем строку в формате json
url = 'https://jsonplaceholder.typicode.com/comments'

python_dict = json.loads(json_data) # Преобразуем эту строку(json) в словарь питона
print(type(python_dict))
print(python_dict)


# GET-запрос
response = requests.get(url)  # делаем запрос по ссылке и получаем ответ в переменную response
data = response.json() # Преобразуем ответ в список со словарями
print('Первый элемент:', data[0]) # Выводим первый элемент списка, словарь

with open('data.json', 'w') as file: # Открывает и записывает в файл .json
    json.dump(data, file, indent=4)


with open('data.json', 'r') as file: # Открывает и читает из файла .json
    python_dict = json.load(file)
print(python_dict)