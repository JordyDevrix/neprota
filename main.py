with open("reken.nept", "r") as file:
    regels = file.readlines()


def haakjes_weg_halen(expression):
    expressie_na_haakjes = expression[1:-1]
    return expressie_na_haakjes


for regel_pre in regels:
    regel = regel_pre.strip().split(" ")

    final = regel[0]
    expressie = regel[1]

    if regel[0] == "REKEN":
        expressie = regel[1]
        var1 = 33
        var2 = 0
        som = ""
        varsomvar = []
        expressie_continuer = ""
        while len(expressie) > 3:
            print(expressie)
            if expressie[0] == "(":
                expressie = haakjes_weg_halen(expressie)

            if expressie[0].isnumeric():
                for karakter, idx in enumerate(expressie):
                    if expressie[karakter] in "+-/*":
                        karaktnum = idx
                        expressie_twee = expressie[karakter+1:]
                        var1 = expressie[0:karakter]
                        som = karaktnum

                        for karakter_twee, idx_twee in enumerate(expressie_twee):
                            if expressie_twee[karakter_twee] in "+-/*":
                                karaktnum = idx_twee
                                var2 = expressie_twee[0:karakter_twee]
                                varsomvar.append(var1)
                                varsomvar.append(som)
                                varsomvar.append(var2)

                            else:
                                continue
                    else:
                        continue

                expressie_continuer = varsomvar[7]

            if expressie_continuer in "+-/*":
                for idx, charact in enumerate(expressie):
                    if charact == "(":
                        expressie = expressie[idx:]

                # print(varsomvar[0:3])

    print(expressie)
