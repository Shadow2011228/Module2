import requests
import json

api_key = '7bff883b746c3b65dc87a2a9784b5bd7'
cities = ['Рутул', 'Махачкала', "Москва"]

list2=[]

for city in cities:
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

  response = requests.get(url)
  data = response.json()
  print(data)

  list2.append(f'Температура: {data['main']["temp"]}\n'
   f'Погода: {data["weather"][0]["description"]}')

  print(f'Температура: {data['main']["temp"]}')
  print(f"Погода: {data["weather"][0]["description"]}")

with open('Cities.json', 'w') as file:
  json.dump(list2, file, indent=4)

