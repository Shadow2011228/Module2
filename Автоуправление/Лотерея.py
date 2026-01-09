import pyautogui
import time
import random

money=300

while money > 0:
    v = random.randint(1, 8)
    money -= 50
    pyautogui.alert(text=f"Ваша ставка 50, осталось {money} руб.", title="Вы начали играть")

    if v == 8:
        pyautogui.alert(text="Вы выиграли +500!", title="Поздравляем!", button="Уpa")
        money+=500
        answer = pyautogui.confirm(text='Продолжить', title='Закончить', buttons= ['Да', 'Нет'])
        if answer=='Нет':
            break

pyautogui.alert(text=f"Вы закончили, теперь у вас {money} руб.", title="Поздравляем!", button="Выйти")