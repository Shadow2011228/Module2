import pyautogui
import time


time.sleep(3)
pyautogui.click(x=873, y=552, button='left')

for i in range(1,5,1):
    pyautogui.dragTo(x=649, y=542+i*20, button='left')
    time.sleep(0.5)
    pyautogui.dragTo(x=758, y=410+i*20, button='left')
    time.sleep(0.5)
    pyautogui.dragTo(x=873, y=552+i*20, button='left')
    time.sleep(0.5)