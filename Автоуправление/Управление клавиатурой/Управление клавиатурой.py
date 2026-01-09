import pyautogui
import time


time.sleep(3)

pyautogui.write('hello') # Имитирует клики по переданному тексту

pyautogui.press('$')

print('Зажатие началось')
pyautogui.keyDown('w')
time.sleep(2)
pyautogui.keyUp('w')
print('Зажатие закончилось')

pyautogui.press('$', presses=4)

with pyautogui.hold('shift'):
    pyautogui.press('2')
    pyautogui.press('1')

pyautogui.hotkey("shift", "1")

pyautogui.write('hello', interval=0.25)

# hello$w$$$$@!!hello