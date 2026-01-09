import requests
import pyautogui


url = "https://reqres.in/api/users"

data={"name":pyautogui.prompt(text="Введите своё имя", title='Поле ввода'), "lastname":pyautogui.prompt(text="Введите свою фамилию", title='Поле ввода')}
pyautogui.alert(text='Вы зарегистрировались!', title='Оповещение', button='OK')

response = requests.post(url, json=data, headers={'x-api-key': 'reqres-free-v1'})
data = response.json()

print(data)

print("Код состояния:", response.status_code)  # Ожидается 201
print("Ответ сервера:", response.text)  # Текст ответа

# text='Вывод данных', title='Вывод данных', button='OK'
pyautogui.alert(text=f'id: {data['id']}', title='Оповещение', button='OK')
pyautogui.alert(text=f"Дата регистрации: {data["createdAt"]}", title='Оповещение', button='OK')
print(f'id: {data['id']}')
print(f"Дата регистрации: {data["createdAt"]}")