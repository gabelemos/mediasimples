import pyautogui
from time import sleep

sleep(3)
print(pyautogui.position())

#alt + tab
pyautogui.keyDown("alt")
sleep(1)
pyautogui.press("tab")
sleep(1)
pyautogui.keyUp("alt")

#def ResumirNotas():
    print("Fazendo cálculos, um momento.")
    pyautogui.press("win")
    pyautogui.write("Chrome")
    pyautogui.press("enter")
    sleep(1)
    pyautogui.click(x=487, y=49)
    pyautogui.write("https://www.siepe.educacao.pe.gov.br/")
    pyautogui.press("enter")
    sleep(1)
    pyautogui.click(x=346, y=117)
    pyautogui.write(login_info[0])
    pyautogui.click(x=579, y=121)
    pyautogui.write(login_info[1])
    pyautogui.press("enter")
    #Turn back the cmd
    pyautogui.keyDown("alt")
    sleep(1)
    pyautogui.press("tab")
    sleep(1)
    pyautogui.keyUp("alt")
    print("Fazendo cálculos, um momento...")

