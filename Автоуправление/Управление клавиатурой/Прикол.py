import time
import pyautogui

clear = "\n" * 50

text = "[][][][][][][][][]"
percent = 0
for slot in range(11):
   print(clear)
   temp = ""
   temp += "[x]" * slot
   temp += "[]" * (10 - slot)
   print("Загрузка...")
   print(temp)
   time.sleep(1)

pyautogui.hotkey("command", "f4")
pyautogui.press('return')