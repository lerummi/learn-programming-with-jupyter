import pandas as pd

speisekarte = pd.DataFrame(
    [
        {"Kategorie": "Getränk", "Speise": "Pappiger Milkshake", "Preis (€)": "3.49"},
        {"Kategorie": "Getränk", "Speise": "Müffelnde Cola", "Preis (€)": "1.99"},
        {"Kategorie": "Getränk", "Speise": "Sabberiger Softdrink", "Preis (€)": "2.29"},
        {"Kategorie": "Getränk", "Speise": "Käselüftender Soda", "Preis (€)": "2.49"},
        {"Kategorie": "Vorspeise", "Speise": "Gammelige Onion Rings", "Preis (€)": "3.99"},
        {"Kategorie": "Vorspeise", "Speise": "Bröselige Nachos", "Preis (€)": "4.49"},
        {"Kategorie": "Vorspeise", "Speise": "Matschepampige Mozzarella Sticks", "Preis (€)": "3.79"},
        {"Kategorie": "Vorspeise", "Speise": "Quatschiger Salat", "Preis (€)": "2.99"},
        {"Kategorie": "Hauptmahlzeit", "Speise": "Ranziger Burger", "Preis (€)": "6.49"},
        {"Kategorie": "Hauptmahlzeit", "Speise": "Knusprig-Matschige Pommes", "Preis (€)": "2.79"},
        {"Kategorie": "Hauptmahlzeit", "Speise": "Schmierlappiger Cheeseburger", "Preis (€)": "5.89"},
        {"Kategorie": "Hauptmahlzeit", "Speise": "Wabberiger Hotdog", "Preis (€)": "3.99"},
        {"Kategorie": "Hauptmahlzeit", "Speise": "Zotteliger Wrap", "Preis (€)": "5.29"},
        {"Kategorie": "Hauptmahlzeit", "Speise": "Schmaddeliger Chickenburger", "Preis (€)": "5.79"},
        {"Kategorie": "Hauptmahlzeit", "Speise": "Brotzeliger Fishburger", "Preis (€)": "5.99"},
        {"Kategorie": "Hauptmahlzeit", "Speise": "Quakige Quesadilla", "Preis (€)": "4.69"},
        {"Kategorie": "Hauptmahlzeit", "Speise": "Zähschleimiger Burrito", "Preis (€)": "6.39"},
        {"Kategorie": "Hauptmahlzeit", "Speise": "Matschfrische Pizza", "Preis (€)": "7.49"},
        {"Kategorie": "Hauptmahlzeit", "Speise": "Käsefußige Tenders", "Preis (€)": "4.49"},
        {"Kategorie": "Hauptmahlzeit", "Speise": "Käsig-Schleimige Wings", "Preis (€)": "4.99"},
        {"Kategorie": "Nachspeise", "Speise": "Matschpampeartiger Donut", "Preis (€)": "2.49"},
        {"Kategorie": "Nachspeise", "Speise": "Schmodderiger Muffin", "Preis (€)": "2.49"},
        {"Kategorie": "Nachspeise", "Speise": "Wurstiger Brownie", "Preis (€)": "2.99"},
        {"Kategorie": "Nachspeise", "Speise": "Sabberleckerer Pancake", "Preis (€)": "3.19"},
        {"Kategorie": "Nachspeise", "Speise": "Klätschige Waffle", "Preis (€)": "3.49"},
        {"Kategorie": "Nachspeise", "Speise": "Verschimmeltes Garlic Bread", "Preis (€)": "2.89"},
        {"Kategorie": "Nachspeise", "Speise": "Käseschimmeliger Croissant", "Preis (€)": "2.49"},
        {"Kategorie": "Nachspeise", "Speise": "Muffeliges Ice Cream", "Preis (€)": "2.49"}
    ]
).set_index(["Kategorie", "Speise"])
