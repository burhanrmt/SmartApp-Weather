import json
from urllib.request import urlopen
from urllib.error import URLError

from sprint1 import weerstation
from sprint2 import smart_app_controller


def actuele_temperatuur():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=52.0907&longitude=5.1214"
        "&current=temperature_2m"
    )

    try:
        antwoord = urlopen(url, timeout=10)
        gegevens = json.loads(antwoord.read().decode("utf-8"))
        antwoord.close()

        temperatuur = gegevens["current"]["temperature_2m"]

        print(
            "De actuele temperatuur in Utrecht is",
            temperatuur,
            "graden Celsius."
        )

    except (URLError, ValueError, KeyError, TimeoutError):
        print("De actuele temperatuur kon niet worden opgehaald.")


def menu():
    while True:
        print("\n========== SMART APP ==========")
        print("1. Actuele temperatuur Utrecht")
        print("2. Weerstation (Sprint 1)")
        print("3. Smart App instellingen (Sprint 2)")
        print("4. Stoppen")

        keuze = input("Maak je keuze: ")

        if keuze == "1":
            actuele_temperatuur()

        elif keuze == "2":
            weerstation()

        elif keuze == "3":
            smart_app_controller()

        elif keuze == "4":
            print("Smart App afgesloten.")
            break

        else:
            print("Ongeldige keuze. Kies 1, 2, 3 of 4.")


if __name__ == "__main__":
    menu()