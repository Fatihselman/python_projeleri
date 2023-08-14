import pyautogui
import time 
import os

count = int(input("sayı girin: "))
mesaj = input("mesaj girin: ")

second=10

while (second>0):
    os.system("cls")
    print(f"başlamak için son {second} saniye....")
    time.sleep(1)
    second -=1

while (count>0):
    pyautogui.typewrite(mesaj)
    pyautogui.press("Enter")

    count -= 1

print("Sonlandı")