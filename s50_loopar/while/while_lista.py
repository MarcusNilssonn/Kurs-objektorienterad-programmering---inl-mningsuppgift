def jämna_tal(heltal):
    tal = 0
    jämna_tal_lista = []

    while tal < heltal:
        for x in range(heltal):
            if x % 2 == 0:
                jämna_tal_lista.append(x)
            tal += 1

    return jämna_tal_lista       

