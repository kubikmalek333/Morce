import os
from datetime import datetime

# Čtení a vytvoření slovníku z textového souboru
with open(os.sep.join(["info.txt"]), encoding="utf-8") as soubor:
    morceta = []
    for radek in soubor:
        radek = radek.strip()
        if radek:
            castky = radek.split(";")
            morcata_dict = {
                "jmeno": castky[0],
                "hmotnost": int(castky[1]),
                "datum_narozeni": datetime.strptime(castky[2], "%Y-%m-%d").date(),
                "cena": float(castky[3]),
                "pohlavi": castky[4]
            }
            morceta.append(morcata_dict)

# Výstup načtených dat
for morce in morceta:
    pohlavie_text = "Sameček" if morce['pohlavi'] == 'm' else "Samička"
    cena_se_slevou = morce['cena'] * 0.9
    print(f"{pohlavie_text} morčete jménem: {morce['jmeno']}.")
    print(f"- váží: {morce['hmotnost']} g")
    print(f"- datum narození: {morce['datum_narozeni']}")
    print(f"- cena se slevou 10 %: {cena_se_slevou:.2f} Kč")
    print()