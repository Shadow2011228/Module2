import pyautogui
import time


pyautogui.alert(text='Оповещение', title='Оповещение', button='OK')
pyautogui.confirm (text='Подтверждение', title='Подтверждение', buttons= ['Yes', 'No'])
text = pyautogui.prompt(text='Поле ввода', title='Поле ввода')
password = pyautogui.password(text='Ввод пароля', title='Ввод пароля', default='', mask='**')
print(text)
print(password)