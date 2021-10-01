import pyautogui
import webbrowser as web
from time import sleep

web.open("https://api.whatsapp.com/send/?phone=+573226099206")
sleep(10)

for i in range(10000):
    pyautogui.typewrite("funciona todo raro pero funciona ")
    pyautogui.press("enter")
