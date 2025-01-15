import pandas as pd
import random


lebenspunkte = [
    ["Start", "a", 5],
    ["a", "b", 6],
    ["b", "c", 2],
    ["c", "d", 4],
    ["d", "i", 9],
    ["i", "j", 5],
    ["j", "k", 3],
    ["k", "l", 2],
    ["l", "Zwerg", 2],
    ["Zwerg", "s", 3],
    ["s", "t", 2],
    ["t", "w", 3],
    ["s", "v", 9],
    ["l", "Riese", 2],
    ["Riese", "u", 2],
    ["u", "y", 3],
    ["d", "n", 10],
    ["n", "s", 7],
    ["c", "f", 2],
    ["f", "m", 4],
    ["m", "Magier", 3],
    ["f", "o", 3],
    ["o", "p", 3],
    ["p", "q", 6],
    ["q", "r", 5],
    ["c", "e", 3],
    ["e", "g", 4],
    ["e", "o", 2],
    ["g", "Hexe", 2],
    ["g", "r", 5],
    ["r", "v", 8],
    ["v", "h", 2],
    ["v", "y", 12],
    ["y", "x", 2],
    ["y", "z", 6],
    ["z", "Schatz", 3]
]

for weg in lebenspunkte:
    start, end, kosten = weg
    exec(f"{start}_{end} = {kosten}")
    exec(f"{end}_{start} = {kosten}")


lebenspunkte = pd.DataFrame(
    lebenspunkte,
    columns=["von", "bis", "Lebenspunkte"]
)


def veraendere_lebenspunkte(lebenspunkte, random_state=42):
    random.seed(random_state)
    lebenspunkte["Lebenspunkte"] = lebenspunkte["Lebenspunkte"].apply(
        lambda x: 
            (1000 * max(0.01, x * ( 0.5 + 1.5 * random.random()))) // 1 / 1000
    )
    return lebenspunkte


def lebenspunkte_als_variablen(lebenspunkte) -> dict:

    vars = {}
    for _, row in lebenspunkte.iterrows():
        start, end, kosten = row
        vars[f"{start}_{end}"] = kosten
    return vars
