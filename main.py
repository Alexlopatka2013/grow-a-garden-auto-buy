import pyautogui
import time

print("Bot startuje za 5 sekund...")
time.sleep(5)

last_afk = time.time()

while True:
    # 🔹 Otwórz sklep
    print("Otwieram sklep...")
    pyautogui.press("e")
    time.sleep(2)

    # 🔹 Kliknij GUI żeby scroll działał
    pyautogui.click(600, 300)
    time.sleep(0.5)

    # 🔹 Scroll 23 razy
    print("Scrolluję...")
    for i in range(23):
        pyautogui.scroll(-120)
        time.sleep(0.05)

    # 🔹 Klik bambus
    print("Klikam bambus...")
    pyautogui.click(1242, 756)
    time.sleep(1)

    # 🔹 Klik kup 27 razy
    print("Kupuję 27 razy...")
    for i in range(27):
        pyautogui.click(1259, 599)
        time.sleep(0.3)

    # 🔹 ANTY AFK (skakanie)
    if time.time() - last_afk > 15:
        print("Anty AFK - skok")
        pyautogui.press("space")
        time.sleep(0.5)
        last_afk = time.time()

    print("Czekam 5 sekund...")
    time.sleep(5)
