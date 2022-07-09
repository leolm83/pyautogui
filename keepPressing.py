import pyautogui
import keyboard

while True:
    pyautogui.press('space')
    if keyboard.is_pressed("p"):
        print("You pressed p")
        break
#o codigo abaixo faz o mesmo, mas obviamente não printa "apertei espaço"
#pyautogui.press('space', presses=5)