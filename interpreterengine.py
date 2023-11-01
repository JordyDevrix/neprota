import sys
from if_statements import *
from booleans import *
from berekeningen import *
from wiskunde import *
from functies_engine import *
from bijwerken import *

bestands_pad = sys.argv[1]
# bestands_pad = "script.nept"

programma_regels = []
with open(bestands_pad, "r") as bestand:
    bestand_regels = bestand.readlines()
    for regel in bestand_regels:
        programma_regels.append(regel.strip())


programma_instructie = []
token_teller = 0
in_aantal_functies = 0
skippen = False
functies = {}
variabele = {}
functie_to_skip = 0

for indx, regel in enumerate(programma_regels):
    idx = indx + 1
    commando_delen = regel.split(" ")
    commando = commando_delen[0]

# SKIPPEN VAN IF STATEMENTS
    if commando_delen[0] == "}":
        in_aantal_functies -= 1
        if in_aantal_functies == functie_to_skip:
            skippen = False

# COMMENTS
    if commando_delen[0].startswith("#"):
        continue

# SCHRIJVEN
    if commando_delen[0] == "SCHRIJF" and not skippen:
        zin = []
        iets = commando_delen[1:]
        for woord in iets:
            bewerkt_woord = woord.replace('"', '').strip()
            if bewerkt_woord.startswith("%") and bewerkt_woord.endswith("%"):
                variabelnaam = bewerkt_woord.replace("%", "")
                variabele_x = {}
                for variabelen in variabele:
                    variabel = variabelen.replace("$", "")
                    variabele_x[variabel] = variabele[variabelen]

                if variabelnaam in variabele_x:
                    check = variabele_x[variabelnaam]
                    zin.append(str(check))
                else:
                    print(f"probleem in: {regel}\n\tfout in lijn {idx}: deze variabele is niet gedifinieerd")
                    exit()
            else:
                zin.append(bewerkt_woord)

        tekst = " ".join(zin)
        print(tekst)

# TEXT UIT LEZEN
    if commando_delen[0] == "LEES" and not skippen:
        if len(commando_delen) == 1:
            print(f"probleem in: {regel}\n\tfout in lijn {idx}: repareer alstublieft om door te gaan")
            exit()
        else:
            tekst_in = input(">>>")
            if tekst_in.isalpha():
                varnaam = commando_delen[1]
                variabele[varnaam] = tekst_in
            elif tekst_in.isnumeric():
                varnaam = commando_delen[1]
                variabele[varnaam] = int(tekst_in)

# BASIS BEREKENINGEN
    if commando_delen[0] == "REKEN" and not skippen:
        antwoord = wiskunde_basis(commando_delen)
        if len(commando_delen) > 2:
            if commando_delen[2] == "NAAR":
                if commando_delen[3] in variabele:
                    print(f"probleem in: {regel}\n\tfout in lijn {idx}: dubbele variabele naam")
                    exit()
                else:
                    variabele[commando_delen[3]] = antwoord


# HELE GETALLEN
    if commando_delen[0] == "HEELGETAL" and not skippen:
        if commando_delen[1] in variabele:
            print(f"probleem in: {regel}\n\tfout in lijn {idx}: dubbele variabele naam")
            exit()
        else:
            if len(commando_delen) <= 3 or commando_delen[2].isnumeric():
                print(f"probleem in: {regel}\n\tfout in lijn {idx}: repareer alstublieft om door te gaan")
                exit()
            elif commando_delen[2] == "=":
                getal_waarde = commando_delen[3]
                variabele[commando_delen[1]] = int(getal_waarde)

# KOMMA GETALLEN
    if commando_delen[0] == "KOMMAGETAL" and not skippen:
        if commando_delen[1] in variabele:
            print(f"probleem in: {regel}\n\tfout in lijn {idx}: dubbele variabele naam")
            exit()
        else:
            if len(commando_delen) <= 3:
                print(f"probleem in: {regel}\n\tfout in lijn {idx}: repareer alstublieft om door te gaan")
                exit()
            elif commando_delen[2] == "=":
                getal_waarde = commando_delen[3]
                variabele[commando_delen[1]] = float(getal_waarde)

# TEKST VARIABELEN
    if commando_delen[0] == "TEKST" and not skippen:
        if commando_delen[1] in variabele:
            print(f"probleem in: {regel}\n\tfout in lijn {idx}: dubbele variabele naam")
            exit()
        else:
            stringzin = []
            if commando_delen[1].startswith('"'):
                print(f"probleem in: {regel}\n\tfout in lijn {idx}: repareer alstublieft om door te gaan")
                exit()
            else:
                for word in commando_delen[2:]:
                    stringzin.append(word)
                stringzinbewerkt = " ".join(stringzin).replace('"', '')
                variabele[commando_delen[1]] = stringzinbewerkt

# IF STATEMENTS
    if commando_delen[0] == "ALS":
        if not skippen:
            skippen = uitvoeren_if_stat(commando_delen, variabele, regel, idx)
            if skippen:
                functie_to_skip = in_aantal_functies
        in_aantal_functies += 1

# BOOLEANS MAKEN
    if commando_delen[0] == "WAARHEID" and not skippen:
        if commando_delen[1] in variabele:
            print(f"probleem in: {regel}\n\tfout in lijn {idx}: dubbele variabele naam")
            exit()
        else:
            variabele[commando_delen[1]] = controleren_op_waarheid(commando_delen, regel, idx)

    if commando_delen[0] == "FUNCTIE":
        functie_aanmaken(commando_delen)

    if commando_delen[0] == "DOE" and not skippen:
        functie_draaien(commando_delen)

# VARIABELE BEWERKEN
    if commando_delen[0] == "BIJWERKEN" and not skippen:
        bijwerken_variabele(commando_delen, variabele, regel, idx)

# VARIABELEN DEFINEREN
    if commando_delen[0] == "DEFINEER" and not skippen:
        for deel in commando_delen:
            if ";" in deel:
                if commando_delen[2].startswith('"'):
                    print(f"probleem in: {regel}\n\tfout in lijn {idx}: TEKST kan niet gedefinieerd worden")
                    exit()
                else:
                    variabele[f"${commando_delen[1]}"] = commando_delen[2].replace(";", "")

    # print(skippen, in_aantal_functies, functie_to_skip, "op regelnummer", idx)
    # print("aantal func: ", in_aantal_functies, "op regel", idx)

