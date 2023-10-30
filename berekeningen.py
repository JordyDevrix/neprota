

def basis_berekening(commando_delen, variabele):
    if commando_delen[-2] == "NAAR":
        index = 3
    else:
        index = 1

    operator = commando_delen[-index]
    som = []
    # PLUSSEN
    uitkomst = 0
    if operator == "+":
        for waarde in commando_delen[1:-index]:
            getal = variabele[waarde]
            som.append(getal)
        uitkomst = sum(som)
    # VERMENIGVULDIGEN
    if operator == "*":
        for waarde in commando_delen[1:-index]:
            getal = variabele[waarde]
            som.append(getal)
        resultaat = 1
        for nummer in som:
            resultaat = resultaat * nummer
        uitkomst = resultaat
    # DELEN
    if operator == "/":
        for waarde in commando_delen[1:-index]:
            getal = variabele[waarde]
            som.append(getal)
        resultaat = som[0]
        for nummer in som[1:]:
            resultaat = resultaat / nummer
        uitkomst = resultaat
    # MINNEN
    if operator == "-":
        for waarde in commando_delen[1:-index]:
            getal = variabele[waarde]
            som.append(getal)
        resultaat = som[0]
        for nummer in som[1:]:
            resultaat = resultaat - nummer
        uitkomst = resultaat

    variabele[commando_delen[-1]] = uitkomst
    return variabele
