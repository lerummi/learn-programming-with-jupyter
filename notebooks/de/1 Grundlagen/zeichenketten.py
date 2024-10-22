import random

class Produkt:

    adjektive = [
        "Matschepampig",
        "Schlabberig",
        "Gammelig",
        "Ranzig",
        "Müffelnd",
        "Pampig",
        "Matschig",
        "Quatschig",
        "Glibberig",
        "Schleimig",
        "Wabberig",
        "Furztriefend",
        "Modrig",
        "Käsig",
        "Muffelig",
        "Bröselig",
        "Schlabbrig",
        "Rotzig",
        "Schlotzig",
        "Klumpig",
        "Ranzelbummelig",
        "Batzig",
        "Miefend",
        "Gatschig",
        "Schmierig",
        "Zerlumpt",
        "Schmodderig",
        "Versifft",
        "Brabbelig",
        "Knorzig",
        "Quakig",
        "Schmaddelig",
        "Brotzelig",
        "Krümelig",
        "Matschknusprig",
        "Verdorben",
        "Klebberig",
        "Schmierlappig",
        "Zottelig",
        "Schlunzig",
        "Muffig",
        "Rotzig",
        "Zähschleimig",
        "Schubbelig",
        "Käsefußig",
        "Matschbrotig",
        "Verwabbert",
        "Labberig",
        "Quatschbrotig",
        "Rotzfrech",
        "Matscheklumpig",
        "Schleimig",
        "Stinkstiefelig",
        "Brotzelig",
        "Pupsig",
        "Schmotzig",
        "Matschfrisch",
        "Sabberig",
        "Klätschnass",
        "Ranzkäseartig",
        "Zwiebelig",
        "Brotig",
        "Fetttriefend",
        "Knüppelig",
        "Klumpig",
        "Glitschig",
        "Schrottig",
        "Pappig",
        "Stinkig",
        "Furzig",
        "Feuchtbröselig",
        "Schleimhautig",
        "Knorpsig",
        "Bratzig",
        "Verschimmelt",
        "Muffelkäseartig",
        "Schwabbelig",
        "Wurstig",
        "Krümelig",
        "Klatschnass",
        "Sabberlappig",
        "Quaddelig",
        "Rotzbrotig",
        "Labbrig",
        "Schlabbrig",
        "Quatschig",
        "Schmandig",
        "Matschpampeartig",
        "Quiekig",
        "Ranzverziert",
        "Schmutzig",
        "Zerlumpft",
        "Käselüftend",
        "Sabberlecker",
        "Schmodderkäseartig",
        "Verschmutzt",
        "Schleimkäse",
        "Gatschbrotig",
        "Käseschimmelig",
        "Klätschig",
        "Bröselmatschig",
        "Schleimtropfend",
        "Pampig-müffelig",
        "Stinkesauer"
    ]


    mahlzeiten = [
        "Burger",
        "Pommes",
        "Nuggets",
        "Hotdog",
        "Wrap",
        "Pizza",
        "Salat",
        "Taco",
        "Burrito",
        "Schnitzel",
        "Fries",
        "Sandwich",
        "Chicken",
        "Cheeseburger",
        "Milkshake",
        "Soda",
        "Cola",
        "Nachos",
        "Donut",
        "Onion-Rings",
        "Muffin",
        "Brownie",
        "Wings",
        "Chickenburger",
        "Fishburger",
        "Bagel",
        "Croissant",
        "Pita",
        "Falafel",
        "Pancakes",
        "Waffel",
        "Salami-Pizza",
        "Cheeseballs",
        "Curly-Fries",
        "Mozzarella-Sticks",
        "Softdrink",
        "Ice-Cream"
    ]

    @classmethod
    def generiere(cls, anzahl: int=3):
        
        adjektive_list = list(cls.adjektive)
        adjektive = []
        for k in range(anzahl - 1):
            n = random.randint(0, len(adjektive_list) - 1)
            adjektive.append(adjektive_list.pop(n))

        if len(adjektive):
            return " ".join(
                [
                    "-".join(adjektive),
                    random.choice(cls.mahlzeiten)
                ]
            )
        else:
            return random.choice(cls.mahlzeiten)


class AbstraktesObject:

    attribute = [None]

    @classmethod
    def generiere(cls):
        return random.choice(cls.attribute)


    

class Person(AbstraktesObject):
    attribute = [
        "Opa",
        "Meine Katze",
        "Deine Mudder",
        "Bro",
        "Taylor Swift",
        "Greta Thunberg",
        "Christiano Ronaldo",
        "Bernd das Brot",
        "Mahatma Ghandi",
        "Mein Chiropraktiker",
        "Donald Trump",
        "Billie Eilish",
        "Ariana Grande",
        "Bibi",
        "Selena Gomez",
        "Der Papst",
        "Der Bundestrainer",
        "Julian Wirtz",
        "Angela Merkel"
    ]


class Verb(AbstraktesObject):
    attribute = [
        "schmatzt", 
        "mümmelt",
        "liebt" 
        "knabbert", 
        "schlürft", 
        "nascht", 
        "mampft",
        "umschwirrt"
        "kostet", 
        "ext",
        "kaut",
        "schaufelt",
        "schnurrt",
        "klaut",
        "verputzt",
        "schnabuliert",
        "beißt",
        "quält sich mit",
        "stopft",
        "schmatzt genüsslich",
        "zwiebelt",
        "zerlegt"
    ]


class Ort(AbstraktesObject):
    attribute = [
        "auf dem Klo",
        "in der Badewanne",
        "auf einem Einhorn reitend",
        "während einer Achterbahnfahrt",
        "unter Wasser im Pool",
        "auf einem Wolkenkratzerdach",
        "im Flugzeug während der Landung",
        "auf einem Heißluftballon",
        "im Kühlschrank stehend",
        "auf einem Trampolin",
        "im Fahrstuhl feststeckend",
        "im Kinderkarussell",
        "im Tonstudio",
        "in einem Zirkuszelt",
        "auf einem Pferd reitend",
        "in einem U-Boot",
        "auf einem Surfbrett im Ozean",
        "im Weltall mit schwebendem Ketchup",
        "auf einem Kamel in der Wüste",
        "im Freizeitpark auf der Geisterbahn",
        "in der Sauna bei 100 Grad",
        "beim Zahnarzt im Wartezimmer",
        "in einem Heißluftballon über den Alpen",
        "auf einer Wiese voller Schafe",
        "in einem Bällebad für Kinder",
        "auf dem Weihnachtsmarkt im Schnee",
        "auf einer Skipiste in voller Fahrt",
        "beim Yoga in der 'Baum'-Position",
        "auf dem Rücksitz eines Polizeiautos",
        "bei einer Beerdigung",
        "während einer romantischen Bootsfahrt",
        "mitten auf einer Bühne bei einem Theaterstück",
        "auf einem schaukelnden Piratenschiff",
        "im Unterricht",
        "auf dem Festival",
        "im Hinterhof"
    ]

class Begruendung(AbstraktesObject):
    attribute = [
        "wegen dem herrlich kribbelnden Gefühl im Magen",
        "weil das Kind dann einfach mal die Klappe hält",
        "denn es regt die Darmflora an",
        "weil er es liebt, wenn der Hintern Kirmes feiert",
        "weil es ein Freifahrtschein für die Seele ist",
        "weil es an die Kindheit erinnern",
        "weil es Superkräfte entfaltet",
        "weil die Knattergeräusche beim Stuhlganz einfach unverwechselbar sind",
        "denn es ist ein Lied für seine Geschmacksnerven",
        "weil er zum Skat spielen einlädt",
        "wegen der geheimen Zutat, die unsichtbar macht",
        "weil es mehr Liebe enthält als jeder Liebesfilm",
        "weil es einfach hypnotisch wirkft",
        "denn hier gibt es immer eine Portion Glück obendrauf",
        "weil sein Partner beim Essen keine blöden Fragen stellt",
        "wegen der magischen Gewürze, die den Alltag vertreiben",
        "weil es dazu anregt, auf dem Tisch zu tanzen",
        "wegen der sagenhaften Kombination von Geschmack und Geräusch",
        "weil er es mit seinen besten Freunden teilen kann",
        "weil es von allem anderen schlechten ablenkt",
        "weil es wie ein Feuerwerk für den Verdauungstrakt ist",
        "wegen der unsichtbaren Energie, die sie weckt",
        "denn die Essenspausen werden ein wahres Abenteuer",
        "weil der Duft wie ein Magnet wirkt",
        "wegen der Würze, die seine Probleme vertreibt",
        "wegen des unverwechselbaren Geschmacks, der an Einlauf erinnert",
        "weil es hilft die Ex zu vergessen",
        "weil es die Stärke eines Bullen verleiht",
        "denn es verwischt die Grenzen von gutem und schlechtem Geschmack",
        "denn einer geht immer noch rein",
        "weil sowieso alles egal ist",
        "denn morgen ist auch noch ein Tag",
        "denn man lebt nur einmal",
        "weil es die Verstopfung lösst",
        "denn ohne Qual ist langweilig",
        "weil es sonst schlecht wird"
    ]


# Beispiel:
#print(
#    "Hunger? Kommt zu uns! \n" +\
#    Person.generiere() + " " +\
#    Verb.generiere() + " " + Produkt.generiere(3) +\
#    " am Liebsten " + Ort.generiere() +\
#    ", ...\n... " + Begruendung.generiere() + "."
#)