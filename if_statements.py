

def check_voor_bool(variabele_begin, vergelijker, variabele_eind):

    if variabele_begin.isnumeric and variabele_eind.isnumeric:
        if vergelijker == "==" and variabele_begin == variabele_eind:
            return True
        if vergelijker == ">=" and variabele_begin >= variabele_eind:
            return True
        if vergelijker == "<=" and variabele_begin <= variabele_eind:
            return True
        if vergelijker == ">" and variabele_begin > variabele_eind:
            return True
        if vergelijker == "<" and variabele_begin < variabele_eind:
            return True


def uitvoeren_if_stat(commando_delen, variabele, regel, idx):
    waarheidstatus = False
    variabele_x = {}
    for variabelen in variabele:
        variabel = variabelen.replace("$", "")
        variabele_x[variabel] = variabele[variabelen]

    if len(commando_delen) > 4:
        if commando_delen[1] in variabele_x:
            beginwaarde = str(variabele_x[commando_delen[1]])
        else:
            beginwaarde = commando_delen[1]

        if commando_delen[2] in variabele_x:
            eindwaarde = str(variabele_x[commando_delen[3]])
        else:
            eindwaarde = commando_delen[3]

        waarheidstatus = check_voor_bool(beginwaarde, commando_delen[2], eindwaarde)

    elif len(commando_delen) <= 4:
        if commando_delen[1] in variabele_x:
            waarheidstatus = variabele_x[commando_delen[1]]

    if commando_delen[1] == "WAAR" or waarheidstatus:
        if commando_delen[-1] == "{" or commando_delen[-1].endswith("{"):
            skippen = False
            return skippen
    elif commando_delen[1] == "ONWAAR" or not waarheidstatus:
        skippen = True
        return skippen
    else:
        print(f"probleem in: {regel}\n\tfout in lijn {idx}: repareer alstublieft om door te gaan")
        exit()

