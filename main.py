import pyautogui
import time

print("Bot startuje za 5 sekund...")
time.sleep(5)

while True:
    print("Otwieram sklep...")
    pyautogui.press("e")
    time.sleep(2)

    # aktywuj GUI
    pyautogui.click(600, 300)
    time.sleep(0.5)

    # scroll 23 razy
    print("Scrolluję...")
    for i in range(23):
        pyautogui.scroll(-120)
        time.sleep(0.05)

    # klik bambus
    print("Klikam bambus...")
    pyautogui.click(1242, 756)
    time.sleep(1)

    # klik kup 27 razy
    print("Kupuję 27 razy...")
    for i in range(27):
        pyautogui.click(1259, 599)
        time.sleep(0.3)

    print("Czekam 5 sekund...")
    time.sleep(5)
