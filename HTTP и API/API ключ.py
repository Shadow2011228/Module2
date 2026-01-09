import requests


api_key = '3064aa3f0c196942b032b6c4666d3761'
city = 'Омск'

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

response = requests.get(url)
data = response.json()
print(data)