import time
import pydirectinput as pdi
import pyautogui

# =========================
# USTAWIENIA
# =========================

# Twoje współrzędne bambusa
BAMBUS_X = 1242
BAMBUS_Y = 756

# Twoje współrzędne przycisku kupna 700 szekli
KUP_X = 1259
KUP_Y = 599

# Scroll trochę wyżej — było 23, teraz 20
SCROLL_ILE = 20

# Ile razy kliknąć kupno
KUP_ILE_RAZY = 27

# Co ile sekund powtarzać całą akcję
POWTARZAJ_CO_SEKUND = 10

# Ile trzymać E
HOLD_E_SECONDS = 1.2

# Pauzy
pdi.PAUSE = 0.08
pyautogui.PAUSE = 0.08

# Fail-safe: jak mysz pójdzie w róg, skrypt może się zatrzymać
pyautogui.FAILSAFE = True


def nacisnij_e():
    print("Naciskam E...")
    pdi.keyDown("e")
    time.sleep(HOLD_E_SECONDS)
    pdi.keyUp("e")
    time.sleep(1)


def klik(x, y, delay=0.3):
    # pyautogui lepiej ustawia pozycję myszy,
    # pydirectinput robi klik do gry
    pyautogui.moveTo(x, y, duration=0.1)
    time.sleep(0.1)
    pdi.click()
    time.sleep(delay)


# Automatyczny środek ekranu — żeby mysz nie leciała dziwnie w bok
SCREEN_W, SCREEN_H = pyautogui.size()
GUI_X = SCREEN_W // 2
GUI_Y = SCREEN_H // 2

print("Rozdzielczość wykryta:", SCREEN_W, "x", SCREEN_H)
print("Środek ekranu:", GUI_X, GUI_Y)

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

    print("Otwieram sklep z nasionami przez E...")
    nacisnij_e()

    print("Czekam aż GUI sklepu się otworzy...")
    time.sleep(2)

    print("Ustawiam mysz na środek ekranu do scrolla...")
    pyautogui.moveTo(GUI_X, GUI_Y, duration=0.1)
    time.sleep(0.5)

    print("Scrolluję w dół trochę wyżej...")
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
