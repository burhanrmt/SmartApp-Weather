def Fahrenheit(celsius):
    fahrenheit = 32 + (1.8 * celsius)
    return fahrenheit


def gevoelstemperatuur(celsius, wind, vocht):
    resultaat = celsius - (vocht / 100 * wind)
    return resultaat


def weerrapport(celsius, wind, vocht):
    gevoel = gevoelstemperatuur(celsius, wind, vocht)

    if gevoel < 0:
        if wind > 10:
            return "Het is heel koud en het stormt! Verwarming helemaal aan!"
        else:
            return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"

    if gevoel < 10:
        if wind > 12:
            return "Het is best koud en het waait; verwarming aan en roosters dicht!"
        else:
            return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"

    if gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."

    return "Warm! Airco aan!"


def weerstation():
    metingen = []

    for nummer in range(1, 8):
        while True:
            invoer_temp = input(
                "Wat is op dag " + str(nummer) + " de temperatuur[C]: "
            )

            if invoer_temp == "":
                print("bye")
                return

            try:
                temperatuur = float(invoer_temp)
                break
            except ValueError:
                print("Ongeldige invoer. Voer een getal in.")

        while True:
            invoer_wind = input(
                "Wat is op dag " + str(nummer) + " de windsnelheid[m/s]: "
            )

            if invoer_wind == "":
                print("bye")
                return

            try:
                wind = float(invoer_wind)

                if wind < 0:
                    print("De windsnelheid mag niet negatief zijn.")
                else:
                    break
            except ValueError:
                print("Ongeldige invoer. Voer een getal in.")

        while True:
            invoer_vocht = input(
                "Wat is op dag " + str(nummer) + " de vochtigheid[%]: "
            )

            if invoer_vocht == "":
                print("bye")
                return

            try:
                vocht = int(invoer_vocht)

                if vocht < 0 or vocht > 100:
                    print("De vochtigheid moet tussen 0 en 100 liggen.")
                else:
                    break
            except ValueError:
                print("Ongeldige invoer. Voer een geheel getal in.")

        metingen.append(temperatuur)

        fahrenheit = Fahrenheit(temperatuur)
        rapport = weerrapport(temperatuur, wind, vocht)
        gemiddelde = sum(metingen) / len(metingen)

        print("Het is", temperatuur, "C (", fahrenheit, "F)")
        print(rapport)
        print("Gem. temp tot nu toe is", gemiddelde)
        print("======================================")


if __name__ == "__main__":
    weerstation()