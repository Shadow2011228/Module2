import pyautogui
import time

from pyautogui import keyDown, keyUp

time.sleep(3)


for i in range(5):
    pyautogui.mouseDown(button="left")

    keyDown("w")
    time.sleep(0.65)
    keyUp("w")

    keyDown("d")
    time.sleep(0.6)
    keyUp("d")

    keyDown("w")
    time.sleep(0.65)
    keyUp("w")

    time.sleep(0.6)

    keyDown("a")
    time.sleep(0.7)
    keyUp("a")

    keyDown("w")
    time.sleep(0.5)
    keyUp("w")

pyautogui.mouseUp(button="left")