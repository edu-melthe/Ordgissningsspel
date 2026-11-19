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
    
    while antal_fel < max_fel:
        print(f"Ord: {visa_ord(hemligt_ord, gissade_bokstaver)}")
        print(f"Felaktiga bokstäver: {felaktiga_gissningar}")
        print(f"Fel gissningar kvar: {max_fel - antal_fel}")
        print()

        gissning = input("Gissa en bokstav: ").strip().lower()

        if len(gissning) != 1 or not gissning.isalpha():
            print("Ogiltig gissning! Du måste skriva en enda bokstav.\n")
            continue

        if gissning in gissade_bokstaver or gissning in felaktiga_gissningar:
            print(f"Du har redan gissat på bokstaven '{gissning}'.\n")
            continue

        if gissning in hemligt_ord:
            gissade_bokstaver.add(gissning)
            print(f"Bra! Bokstaven '{gissning}' finns i ordet.\n")
        else:
            felaktiga_gissningar.append(gissning)
            antal_fel += 1
            print(f"Tyvärr, '{gissning}' finns inte i ordet.\n")

        if all(bokstav in gissade_bokstaver for bokstav in hemligt_ord):
            print(f"Grattis! Du klarade det! Ordet var: {hemligt_ord}")
            return

    print(f"Tyvärr, du har inga gissningar kvar.")
    print(f"Det rätta ordet var: {hemligt_ord}")

if __name__ == "__main__":
    while True:
        spela()
        igen = input("\nVill du spela igen? (j/n): ").strip().lower()
        if igen != "j":
            print("Tack för att du spelade!")
            break
        print("\n" + "="*40 + "\n")