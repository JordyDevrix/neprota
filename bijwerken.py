

def bijwerken_variabele(commando_delen, variabele, regel, idx):
    zin_delen = []
    try:
        if commando_delen[2] == "=":
            try:
                if commando_delen[1].startswith('$'):
                    print(f"probleem in: {regel}\n\tfout in lijn {idx}: constanten kan je niet bijwerken")
                    exit()
                elif commando_delen[1] in variabele:
                    if commando_delen[3].startswith('"'):
                        for woord in commando_delen[3:]:
                            zin_delen.append(woord)
                            zin = " ".join(zin_delen).replace('"', '')
                            variabele[commando_delen[1]] = zin
                    else:
                        variabele[commando_delen[1]] = commando_delen[3]
                    return variabele
                else:
                    print(f"probleem in: {regel}\n\tfout in lijn {idx}: variabele niet gevonden")
                    exit()
            except IndexError:
                print(f"probleem in: {regel}\n\tfout in lijn {idx}: repareer alstublieft om door te gaan")
                exit()
        else:
            print(f"probleem in: {regel}\n\tfout in lijn {idx}: repareer alstublieft om door te gaan")
            exit()
    except IndexError:
        print(f"probleem in: {regel}\n\tfout in lijn {idx}: repareer alstublieft om door te gaan")
        exit()
