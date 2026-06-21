import time
import pydirectinput as pdi
import pyautogui

# Małe pauzy, żeby Roblox nadążał
pdi.PAUSE = 0.05
pyautogui.PAUSE = 0.05

# Współrzędne z Twojego setupu
BAMBUS_X = 1242
BAMBUS_Y = 756

KUP_X = 1259
KUP_Y = 599

GUI_X = 600
GUI_Y = 300

SCROLL_ILE = 23
KUP_ILE_RAZY = 27


def nacisnij_klawisz(klawisz, czas=0.2):
    pdi.keyDown(klawisz)
    time.sleep(czas)
    pdi.keyUp(klawisz)
    time.sleep(0.2)


def kliknij(x, y, przerwa=0.3):
    pdi.moveTo(x, y)
    time.sleep(0.1)
    pdi.click()
    time.sleep(przerwa)


print("Bot startuje za 7 sekund...")
print("Wejdź teraz do Roblox i kliknij raz w okno gry.")
time.sleep(7)

while True:
    print("Otwieram sklep E...")
    nacisnij_klawisz("e", 0.25)
    time.sleep(2)

    print("Aktywuję GUI sklepu...")
    kliknij(GUI_X, GUI_Y, 0.5)

    print("Scrolluję sklep 23 razy...")
    for i in range(SCROLL_ILE):
        pyautogui.scroll(-120)
        time.sleep(0.05)

    print("Klikam bambus...")
    kliknij(BAMBUS_X, BAMBUS_Y, 1)

    print("Kupuję 27 razy przycisk 700 szekli...")
    for i in range(KUP_ILE_RAZY):
        print(f"Kupowanie {i + 1}/{KUP_ILE_RAZY}")
        kliknij(KUP_X, KUP_Y, 0.25)

    print("Próbuję zamknąć sklep E...")
    nacisnij_klawisz("e", 0.25)
    time.sleep(1)

    print("Anty AFK - skok...")
    nacisnij_klawisz("space", 0.25)

    print("Czekam 5 sekund i powtarzam...")
    time.sleep(5)
