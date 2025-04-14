import csv
from datetime import datetime

def bereken_uren(start, eind):
    tijd_formaat = "%H:%M"
    starttijd = datetime.strptime(start, tijd_formaat)
    eindtijd = datetime.strptime(eind, tijd_formaat)
    verschil = eindtijd - starttijd
    return round(verschil.total_seconds() / 3600, 2)

def main():
    print("Urenregistratie - invoer via command line\n")

    naam = input("Wat is je naam? ")
    datum = input("Datum van de gewerkte dag (YYYY-MM-DD): ")
    starttijd = input("Hoe laat ben je begonnen? (HH:MM): ")
    eindtijd = input("Hoe laat ben je gestopt? (HH:MM): ")
    omschrijving = input("Wat heb je gedaan? (korte omschrijving): ")

    uren = bereken_uren(starttijd, eindtijd)

    rij = [naam, datum, starttijd, eindtijd, uren, omschrijving]

    bestandsnaam = "urenregistratie.csv"
    bestand_bestaat = False

    try:
        with open(bestandsnaam, 'r'):
            bestand_bestaat = True
    except FileNotFoundError:
        pass

    with open(bestandsnaam, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if not bestand_bestaat:
            writer.writerow(["Naam", "Datum", "Starttijd", "Eindtijd", "Aantal uren", "Omschrijving"])
        writer.writerow(rij)

    print("\n✅ Gegevens opgeslagen in:", bestandsnaam)

if __name__ == "__main__":
    main()
