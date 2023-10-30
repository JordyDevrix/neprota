def controleren_op_waarheid(commando_delen, regel, idx):
    if commando_delen[3] == "WAAR":
        return True
    elif commando_delen[3] == "ONWAAR":
        return False
    else:
        print(f"probleem in: {regel}\n"
              f"\tfout in lijn {idx}. onjuiste waarheid?: repareer alstublieft om door te gaan")
        exit()
