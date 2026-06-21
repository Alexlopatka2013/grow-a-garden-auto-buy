import pyautogui
import time
import json

# Wczytanie ustawień z config.json
with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

open_shop_key = config["open_shop_key"]
delay_after_open = config["delay_after_open"]
bamboo_button = config["bamboo_button"]
buy_button = config["buy_button"]

print("Bot startuje za 5 sekund...")
print("Ustaw postać przy sklepie z nasionami.")
time.sleep(5)

print("Naciskam E, żeby otworzyć sklep...")
pyautogui.press(open_shop_key)

time.sleep(delay_after_open)

print("Klikam bambus...")
pyautogui.click(bamboo_button["x"], bamboo_button["y"])

time.sleep(1)

print("Klikam kup za 700 szekli...")
pyautogui.click(buy_button["x"], buy_button["y"])

print("Gotowe! Próba kupienia bambusa zakończona.")
