import pyautogui

MemoryLogin=[]
MemoryPass=[]
Memory={'login':'password'}

def website():
    pyautogui.alert(text='Добро пожаловать на нащ сайт/приложение', title='Website', button='Спасибо')
    otvet=pyautogui.confirm(text='Вы уже зарегистрированы', title='Регистрация', buttons=['Да', 'Нет', 'Выход'])
    if otvet=='Нет':
        pyautogui.alert(text='Тогда вам нужно зарегистрироваться', title='Website', button='Хорошо')
        NewLogin = pyautogui.prompt(text='Введите логин', title='Регистрация')
        NewPassword = pyautogui.password(text='Ввод пароля', title='Ввод пароля', default='', mask='**')
        pyautogui.alert(text='Вы успешно зарегистрировались', title='Регистрация', button='OK')
        Memory[NewLogin]=NewPassword
        website()
        return

    elif otvet=="Да":
        Login=pyautogui.prompt(text='Введите логин', title='Вход')
        Password=pyautogui.password(text='Ввод пароля', title='Ввод пароля', default='', mask='**')
        print(Memory)
        if Login not in Memory:
            pyautogui.alert(text='Вы не верно ввели логин', title='Website', button='Хорошо')
        elif Password != Memory[Login]:
            pyautogui.alert(text='Вы не верно ввели пароль', title='Website', button='Хорошо')
        else:
            pyautogui.alert(text='Вы успешно вошли в аккаунт', title='Website', button='Хорошо')
        website()




website()