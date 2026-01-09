import requests


url = "https://reqres.in/api/users"

data = {
   'name':input("Введите своё имя:"),
    'lastname':input("Введите свою фамилию:")
}
print('Вы зарегистрировались!')

response = requests.post(url, json=data, headers={'x-api-key': 'reqres-free-v1'})
data = response.json()

print("Код состояния:", response.status_code)  # Ожидается 201
print("Ответ сервера:", response.text)  # Текст ответа

print(f'id: {data['id']}')
print(f"Дата регистрации: {data["createdAt"]}")