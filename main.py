import time
import pydirectinput as pdi
import pyautogui

# ===== USTAWIENIA =====

# Kliknięcie w GUI sklepu, żeby scroll działał
GUI_X = 600
GUI_Y = 300

# Pozycja bambusa
BAMBUS_X = 1242
BAMBUS_Y = 756

# Pozycja przycisku kupna 700 szekli
KUP_X = 1259
KUP_Y = 599

# Ile razy scrollować w dół
SCROLL_ILE = 23

# Ile razy kliknąć kupno
KUP_ILE_RAZY = 27

# Co ile sekund powtarzać całą akcję
POWTARZAJ_CO_SEKUND = 10

# Ile trzymać E
HOLD_E_SECONDS = 0.7

pdi.PAUSE = 0.08
pyautogui.PAUSE = 0.08


def klik(x, y, delay=0.3):
    pdi.moveTo(x, y)
    time.sleep(0.1)
    pdi.click()
    time.sleep(delay)


def nacisnij_e():
    print("Naciskam E...")
    pdi.keyDown("e")
    time.sleep(HOLD_E_SECONDS)
    pdi.keyUp("e")
    time.sleep(1)


print("Bot startuje za 10 sekund.")
print("Wejdź do Roblox, stań przy sklepie z nasionami i kliknij raz w okno gry.")
time.sleep(10)

while True:
    print("=== START CYKLU ===")

    # Aktywuj okno Roblox / GUI
    print("Klikam w okno gry...")
    klik(GUI_X, GUI_Y, 0.5)

    # Otwórz sklep E
    print("Otwieram sklep z nasionami...")
    nacisnij_e()

    # Czekaj na GUI sklepu
    print("Czekam na GUI sklepu...")
    time.sleep(2)

    # Kliknij GUI, żeby scroll działał
    print("Aktywuję GUI sklepu...")
    klik(GUI_X, GUI_Y, 0.5)

    # Scroll
    print("Scrolluję w dół...")
    for i in range(SCROLL_ILE):
        pyautogui.scroll(-120)
        time.sleep(0.05)

    # Klik bambus
    print("Klikam bambus...")
    klik(BAMBUS_X, BAMBUS_Y, 1)

    # Klik kup 27 razy
    print("Kupuję 27 razy...")
