import time
import pydirectinput as pdi
import pyautogui

# =========================
# STAŁA POZYCJA MYSZKI
# =========================

# TU MA BYĆ MYSZKA — TWOJE WSPÓŁRZĘDNE
BASE_X = 1275
BASE_Y = 365

# Bambus
BAMBUS_X = 1242
BAMBUS_Y = 756

# Przycisk kupna 700 szekli
KUP_X = 1259
KUP_Y = 599

# Scroll — jeśli dalej za nisko, zmniejsz SCROLL_ILE
SCROLL_ILE = 16
SCROLL_POWER = -100

# Ile razy kupować
KUP_ILE_RAZY = 27

# Co ile sekund powtarzać
POWTARZAJ_CO_SEKUND = 10

# Ile trzymać E
HOLD_E_SECONDS = 1.2

pdi.PAUSE = 0.08
pyautogui.PAUSE = 0.08
pyautogui.FAILSAFE = True


def idz_na_baze():
    # Myszka zawsze wraca tutaj: x=1275 y=365
    pyautogui.moveTo(BASE_X, BASE_Y, duration=0.05)
    time.sleep(0.1)


def nacisnij_e():
    idz_na_baze()
    print("Naciskam E...")
    pdi.keyDown("e")
    time.sleep(HOLD_E_SECONDS)
    pdi.keyUp("e")
    time.sleep(1)
    idz_na_baze()


def klik(x, y, delay=0.25):
    # Klik w danym miejscu
    pyautogui.moveTo(x, y, duration=0.05)
    time.sleep(0.08)
    pdi.click()
    time.sleep(delay)

    # Po kliknięciu NATYCHMIAST wraca na x=1275 y=365
    idz_na_baze()


print("Bot startuje za 10 sekund.")
print("Wejdź do Roblox, stań przy sklepie z nasionami i kliknij raz w okno gry.")
time.sleep(10)

# ustaw myszkę od razu na Twoją pozycję
idz_na_baze()


while True:
    print("================================")
    print("START CYKLU")
    print("================================")

    # najpierw baza
    idz_na_baze()

    print("Otwieram sklep z nasionami przez E...")
    nacisnij_e()

    print("Czekam aż GUI sklepu się otworzy...")
    time.sleep(2)

    print("Ustawiam myszkę na x=1275 y=365 do scrolla...")
    idz_na_baze()

    print("Scrolluję w dół...")
    for i in range(SCROLL_ILE):
        pyautogui.scroll(SCROLL_POWER)
        time.sleep(0.05)

    # po scrollu wraca na bazę
    idz_na_baze()

    print("Klikam bambus...")
    klik(BAMBUS_X, BAMBUS_Y, 1)

    print("Klikam kup 27 razy...")
    for i in range(KUP_ILE_RAZY):
        print(f"Kupowanie {i + 1}/{KUP_ILE_RAZY}")
        klik(KUP_X, KUP_Y, 0.25)

    print("Wracam myszką na x=1275 y=365...")
    idz_na_baze()

    print("KONIEC CYKLU")
    print(f"Czekam {POWTARZAJ_CO_SEKUND} sekund...")
    time.sleep(POWTARZAJ_CO_SEKUND)
