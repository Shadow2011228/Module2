import time
import pyautogui

def mine(sec=1.25):
   pyautogui.mouseDown(button="left")
   time.sleep(sec)
   pyautogui.mouseUp(button="left")

def action(key):
   pyautogui.keyDown(key)
   time.sleep(0.13)
   pyautogui.keyUp(key)

time.sleep(3)
while True:
   mine()
   action('a')
   mine()
   action('d')
   action('w')