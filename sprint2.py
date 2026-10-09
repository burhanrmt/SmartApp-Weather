def aantal_dagen(inputFile):
    bestand = open(inputFile, "r")
    regels = bestand.readlines()
    bestand.close()
    return len(regels) - 1


def auto_bereken(inputFile, outputFile):
    bestand = open(inputFile, "r")
    regels = bestand.readlines()
    bestand.close()

    uitvoer = open(outputFile, "w")

    for nummer in range(1, len(regels)):
        gegevens = regels[nummer].split()

        if len(gegevens) < 5:
            continue

        datum = gegevens[0]
        personen = int(gegevens[1])
        tempSetpoint = float(gegevens[2])
        tempOutside = float(gegevens[3])
        neerslag = float(gegevens[4])

        verschil = tempSetpoint - tempOutside

        if verschil >= 20:
            cv = 100
        elif verschil >= 10:
            cv = 50
        else:
            cv = 0

        ventilatie = personen + 1
        if ventilatie > 4:
            ventilatie = 4

        if neerslag < 3:
            bewatering = True
        else:
            bewatering = False

        uitvoer.write(
            datum + ";" + str(cv) + ";" +
            str(ventilatie) + ";" + str(bewatering) + "\n"
        )

    uitvoer.close()


def overwrite_settings(outputFile):
    bestand = open(outputFile, "r")
    regels = bestand.readlines()
    bestand.close()

    datum_gezocht = input("Voor welke datum wil je instellingen aanpassen? ")
    gevonden = False

    for nummer in range(len(regels)):
        gegevens = regels[nummer].strip().split(";")

        if len(gegevens) < 4:
            continue

        if gegevens[0] == datum_gezocht:
            gevonden = True

            systeem = input(
                "Welk systeem wil je aanpassen? "
                "1 = CV, 2 = ventilatie, 3 = bewatering: "
            )

            if systeem == "1":
                waarde = input("Nieuwe CV-waarde (0 t/m 100): ")

                try:
                    waarde = int(waarde)
                except ValueError:
                    return -3

                if waarde < 0 or waarde > 100:
                    return -3

                gegevens[1] = str(waarde)

            elif systeem == "2":
                waarde = input("Nieuwe ventilatiewaarde (0 t/m 4): ")

                try:
                    waarde = int(waarde)
                except ValueError:
                    return -3

                if waarde < 0 or waarde > 4:
                    return -3

                gegevens[2] = str(waarde)

            elif systeem == "3":
                waarde = input("Nieuwe bewatering (0 = False, 1 = True): ")

                if waarde == "0":
                    gegevens[3] = "False"
                elif waarde == "1":
                    gegevens[3] = "True"
                else:
                    return -3
            else:
                return -3

            regels[nummer] = ";".join(gegevens) + "\n"
            break

    if not gevonden:
        return -1

    bestand = open(outputFile, "w")

    for regel in regels:
        bestand.write(regel)

    bestand.close()

    return 0


def smart_app_controller():
    while True:
        print("\n===== SMART APP INSTELLINGEN =====")
        print("1. Aantal dagen bekijken")
        print("2. Instellingen automatisch berekenen")
        print("3. Instellingen aanpassen")
        print("4. Terug naar hoofdmenu")

        keuze = input("Maak je keuze: ")

        if keuze == "1":
            try:
                aantal = aantal_dagen("weerdata.txt")
                print("Aantal dagen:", aantal)
            except FileNotFoundError:
                print("Het bestand weerdata.txt is niet gevonden.")

        elif keuze == "2":
            try:
                auto_bereken("weerdata.txt", "uitvoer.txt")
                print("Instellingen zijn opgeslagen in uitvoer.txt.")
            except FileNotFoundError:
                print("Het bestand weerdata.txt is niet gevonden.")
            except (ValueError, IndexError):
                print("Er staat ongeldige data in weerdata.txt.")

        elif keuze == "3":
            try:
                resultaat = overwrite_settings("uitvoer.txt")

                if resultaat == 0:
                    print("Instellingen zijn aangepast.")
                elif resultaat == -1:
                    print("Deze datum is niet gevonden.")
                elif resultaat == -3:
                    print("Ongeldig systeem of ongeldige waarde.")

            except FileNotFoundError:
                print("Maak eerst het uitvoerbestand via optie 2.")

        elif keuze == "4":
            break
        else:
            print("Ongeldige keuze. Kies 1, 2, 3 of 4.")


if __name__ == "__main__":
    smart_app_controller()