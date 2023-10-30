

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


def uitvoeren_if_stat(commando_delen, variabele, in_aantal_functies):
    waarheidstatus = False
    if len(commando_delen) > 4:
        if commando_delen[1] in variabele:
            beginwaarde = str(variabele[commando_delen[1]])
        else:
            beginwaarde = commando_delen[1]

        if commando_delen[2] in variabele:
            eindwaarde = str(variabele[commando_delen[3]])
        else:
            eindwaarde = commando_delen[3]

        waarheidstatus = check_voor_bool(beginwaarde, commando_delen[2], eindwaarde)

    elif len(commando_delen) <= 4:
        if commando_delen[1] in variabele:
            waarheidstatus = variabele[commando_delen[1]]

    if commando_delen[1] == "WAAR" or waarheidstatus:
        if commando_delen[-1] == "{" or commando_delen[-1].endswith("{"):
            skippen = False
            return skippen
    elif commando_delen[1] == "ONWAAR" or not waarheidstatus:
        skippen = True
        return skippen

