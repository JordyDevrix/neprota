"""
with open("reken.nept", "r") as file:
    regels = file.readlines()


for regel_pre in regels:
    regel = regel_pre.strip().split(" ")

    final = regel[0]
    expressie = regel[1]
    answer = False

    if regel[0] == "REKEN":
"""


def wiskunde_basis(regel):
    expressie = regel[1]
    expressie_delen = []
    haakjes = 0
    skipcounter = 0
    # print("step 1: ", expressie)
    for idx, karakter in enumerate(expressie):
        if skipcounter > 0:
            skipcounter -= 1
        elif skipcounter == 0:
            if expressie[idx] == "(":
                haakjes += 1
                expressie_delen.append(karakter)

            elif expressie[idx] == ")":
                haakjes -= 1
                expressie_delen.append(karakter)

            elif expressie[idx] == " ":
                continue

            elif expressie[idx] in "+-/*":
                haakjes -= 1
                expressie_delen.append(karakter)

            elif expressie[idx].isnumeric():
                expressie_reverse = expressie[idx:][::-1]
                # print(expressie_reverse)
                for nummer in range(len(expressie_reverse)):
                    if expressie_reverse[nummer:].replace(".", "1").isnumeric():
                        if len(expressie_reverse[nummer:]) > 1:
                            skipcounter = len(expressie_reverse[nummer:]) - 1
                            # print("MATCH:", expressie_reverse[nummer:][::-1])
                            expressie_delen.append(expressie_reverse[nummer:][::-1])
                            break
                        elif len(expressie_reverse[nummer:]) == 1:
                            expressie_delen.append(expressie_reverse[nummer:])
            elif expressie[idx] == "P":
                if expressie[idx+1] == "I":
                    skipcounter = 1
                    expressie_delen.append("3.14159265359")
            else:
                print("An un processable character was found at", idx)
                exit()
    # print("step 2: ", expressie_delen)
    uitkomst = "".join(expressie_delen)
    # print("step 3: ", uitkomst)
    # print("step 4: ", eval(uitkomst))
    return eval(uitkomst)


"""
    levelcounter = 0
    levelavarage = []
    for idx, levels in enumerate(expressie_delen):
        if levels == "(":
            levelcounter += 1
            levelavarage.append(levelcounter)

        elif levels == ")":
            levelcounter -= 1
            levelavarage.append(levelcounter)

        else:
            levelavarage.append(levelcounter)

    # print(levelavarage)
"""

