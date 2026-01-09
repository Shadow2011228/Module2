import pyautogui
import time

from pyautogui import keyDown, keyUp

time.sleep(3)

with pyautogui.hold('shift'):
    pyautogui.click(x=830, y=467, button='right')
with pyautogui.hold('shift'):
    pyautogui.click(x=761, y=628, button='left')
with pyautogui.hold('shift'):
    pyautogui.click(x=725, y=630, button='right')
time.sleep(10)
pyautogui.click(x=826, y=408, button='left')
pyautogui.click(x=657, y=611, button='left')

pyautogui.press('esc')

keyDown("d")
time.sleep(0.1)
keyUp("d")

for i in range(1):

    pyautogui.click(x=830, y=467, button='right')
    pyautogui.click(x=649, y=632, button='left')
    pyautogui.click(x=696, y=384, button='right')
    pyautogui.click(x=684, y=404, button='right')
    pyautogui.click(x=649, y=632, button='left')
    pyautogui.click(x=681, y=625, button='left')
    pyautogui.click(x=693, y=446, button='right')
    pyautogui.click(x=681, y=625, button='left')

    # keyDown("shift")
    # pyautogui.click(x=919, y=380, button='left')
    # time.sleep(1)
    # keyUp("shift")

    with pyautogui.hold('shift'):
        pyautogui.click(x=843, y=408, button='left')


    pyautogui.press('esc')