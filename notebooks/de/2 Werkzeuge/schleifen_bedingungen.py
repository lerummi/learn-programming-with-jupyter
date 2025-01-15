import random
import pandas as pd

from funktionen import edges as verbindungen

verbindungen = pd.DataFrame(verbindungen, columns=["von", "bis", "Lebenspunkte"])
verbindungen = pd.concat(
    [
        verbindungen,
        verbindungen.rename(columns={"von": "bis", "bis": "von"})
    ], axis=0
)

def nachbarpunkte(punkt: str):

    return (
        verbindungen
        .query("von == @punkt")["bis"]
        .sample(frac=1.0)
        .tolist()
    )

def kosten(start: str, ende: str):

    wert = (
        verbindungen
        .query("von == @start and bis == @ende")
        ["Lebenspunkte"]
    )
    
    if len(wert):
        return float(wert.values[0])
    else:
        raise ValueError(f"Die Verbindung {start} -> {ende} existiert nicht.")


def einmal_wuerfeln():
    """
    Das Aufrufen dieser Funktion gibt eine zufällige Zahl zwischen 1 und 6 aus.
    """
    return random.randint(1, 6)


def erstelle_tabelle_ohne_duplikate(ergebnisse):

    tabelle = pd.DataFrame(ergebnisse, columns=["Weg", "Gesamtkosten"])
    tabelle["hash"] = tabelle["Weg"].apply("".join)
    tabelle.drop_duplicates(inplace=True, subset=["hash"])
    tabelle.drop(columns=["hash"], inplace=True)
    tabelle.sort_values(by="Gesamtkosten", ascending=True, inplace=True)
    tabelle.reset_index(drop=True)
    return tabelle 


def musterloesung_weg():

    mein_ort = "Start"
    mein_ziel = "Schatz"
    mein_weg = [mein_ort]
    meine_kosten = 0

    # Solange ich noch nicht am Ziel bin
    while mein_ort != mein_ziel:
        print("Mein Ort:", mein_ort)
        print("Bisherige Kosten:", meine_kosten)

        nachbarn = nachbarpunkte(mein_ort)
        # Iteriere über die Nachbarpunkte, und gehe zu einem Nachbarn, 
        # der noch nicht auf dem Weg ist
        for nachbar in nachbarn:
            if nachbar not in mein_weg:
                meine_kosten = meine_kosten + kosten(mein_ort, nachbar)
                mein_ort = nachbar
                mein_weg.append(mein_ort)
                # Breche die Vorschleife ab
                break
            else:
                # Speichere einen Nachbarn, der schon auf dem Weg ist
                nachbar_auf_dem_weg = nachbar

        # Prüfe, wir nicht auf einem Nachbarn der Liste stehen, wenn doch, gehe
        # zum gespeicherten Nachbarn
        if mein_ort != nachbar:
            print("Nachbar schon auf dem Weg")
            meine_kosten = meine_kosten + kosten(mein_ort, nachbar_auf_dem_weg)
            mein_ort = nachbar_auf_dem_weg
            mein_weg.append(mein_ort)

    return mein_weg, meine_kosten
