import time
import pydirectinput as pdi
import pyautogui

# ===== TWOJE USTAWIENIA =====

# Kliknięcie w środek GUI/sklepu, żeby scroll działał
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

# Ile trzymać E
# Jak zwykłe kliknięcie E nie działa, zwiększ na 1.0 albo 1.5
HOLD_E_SECONDS = 0.5

# Pauzy
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
print("TERAZ wejdz do Roblox, stan przy sklepie z nasionami i kliknij raz w okno gry.")
time.sleep(10)

# Klik w Roblox, żeby gra dostała focus
print("Aktywuję Roblox kliknięciem w środek ekranu...")
klik(GUI_X, GUI_Y, 0.5)

# Otwórz sklep
print("Otwieram sklep z nasionami przez E...")
nacisnij_e()

# Poczekaj aż GUI sklepu się pokaże
print("Czekam na GUI sklepu...")
time.sleep(2)

# Klik w GUI sklepu
print("Klikam GUI sklepu...")
klik(GUI_X, GUI_Y, 0.5)

# Scroll
print("Scrolluję w dół...")
for i in range(SCROLL_ILE):
    pyautogui.scroll(-120)
    time.sleep(0.05)

# Klik bambus
print("Klikam bambus...")
klik(BAMBUS_X, BAMBUS_Y, 1)

# Kup 27 razy
print("Kupuję 27 razy...")
for i in range(KUP_ILE_RAZY):
    print(f"Kupowanie {i + 1}/{KUP_ILE_RAZY}")
    klik(KUP_X, KUP_Y, 0.25)

print("Gotowe ✅")
