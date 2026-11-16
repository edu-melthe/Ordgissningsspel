import random

ordlista = [
    "python", "programmering", "dator", "skola", "lärare",
    "elev", "projekt", "nikodemus", "teknik", "moped",
    "skidor", "vinter", "sommar", "höst", "vår",
    "äpple", "banan", "julafton", "höstlov", "sverige",
    "bil", "cykel", "tåg", "flygplan", "båt",
    "motor", "katt", "fågel", "förgasare", "åva","danielmontenegrovanner"
]
def visa_ord(ord, gissade_bokstaver):
    """Returnerar ordet med stjärnor för ogissade bokstäver"""
    resultat = ""
    for bokstav in ord:
        if bokstav in gissade_bokstaver:
            resultat += bokstav + " "
        else:
            resultat += "* "
    return resultat.strip()

def spela():
    hemligt_ord = random.choice(ordlista).lower()
    gissade_bokstaver = set()
    felaktiga_gissningar = []
    max_fel = 9
    antal_fel = 0

    print("ORDGISSNINGSSPEL")
    print(f"Ordet har {len(hemligt_ord)} bokstäver.")
    print()