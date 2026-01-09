import requests


url = "https://rebotica.free.beeceptor.com"

data = {
   "name": "Иван",
   "job": "Программист"
}

# POST-запрос
response = requests.post(url, json=data)

# Вывод результата
print("Код состояния:", response.status_code)  # Ожидается 201
print("Ответ сервера:", response.text)  # Текст ответа