import time
import pydirectinput as pdi
import pyautogui

# =========================
# USTAWIENIA POD 2K 2560x1440
# =========================

# Środek ekranu / GUI sklepu dla 2K
GUI_X = 1280
GUI_Y = 720

# Twoje współrzędne bambusa
BAMBUS_X = 1242
BAMBUS_Y = 756

# Twoje współrzędne przycisku kupna 700 szekli
KUP_X = 1259
KUP_Y = 599

# Ile razy scrollować w dół
SCROLL_ILE = 23

# Ile razy kliknąć kupno
KUP_ILE_RAZY = 27

# Co ile sekund powtarzać całą akcję
POWTARZAJ_CO_SEKUND = 10

# Ile trzymać E
HOLD_E_SECONDS = 1.2

# Pauzy, żeby Roblox nadążał
pdi.PAUSE = 0.08
pyautogui.PAUSE = 0.08

# Fail-safe: jak mysz pójdzie w róg ekranu, PyAutoGUI może zatrzymać skrypt
pyautogui.FAILSAFE = True


def nacisnij_e():
    print("Naciskam E...")
    pdi.keyDown("e")
    time.sleep(HOLD_E_SECONDS)
    pdi.keyUp("e")
    time.sleep(1)


def klik(x, y, delay=0.3):
    pdi.moveTo(x, y)
    time.sleep(0.1)
    pdi.click()
    time.sleep(delay)


print("Bot startuje za 10 sekund.")
print("WEJDŹ DO ROBLOX.")
print("STAŃ PRZY SKLEPIE Z NASIONAMI.")
print("KLIKNIJ RAZ W OKNO GRY, ŻEBY ROBLOX BYŁ AKTYWNY.")
print("Nie klikaj PowerShella po starcie.")
time.sleep(10)


while True:
    print("================================")
    print("START CYKLU")
    print("================================")

    # Ważne: nie klikamy na początku w Windows,
    # bo Roblox ma być już aktywny po Twoim kliknięciu.

    print("Otwieram sklep z nasionami przez E...")
    nacisnij_e()

    print("Czekam aż GUI sklepu się otworzy...")
    time.sleep(2)

    print("Ustawiam mysz nad środkiem sklepu do scrolla...")
    pdi.moveTo(GUI_X, GUI_Y)
    time.sleep(0.5)

    print("Scrolluję w dół...")
    for i in range(SCROLL_ILE):
        pyautogui.scroll(-120)
        time.sleep(0.05)

    print("Klikam bambus...")
    klik(BAMBUS_X, BAMBUS_Y, 1)

    print("Klikam kup 27 razy...")
    for i in range(KUP_ILE_RAZY):
        print(f"Kupowanie {i + 1}/{KUP_ILE_RAZY}")
        klik(KUP_X, KUP_Y, 0.25)

    print("KONIEC CYKLU")
    print(f"Czekam {POWTARZAJ_CO_SEKUND} sekund...")
    time.sleep(POWTARZAJ_CO_SEKUND)
``
