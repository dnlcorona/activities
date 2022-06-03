def tratamento(arg1):
    palavroes = ["babaca", "pilantra", "retardado", "retardada", "burro", "burra", "feio", "feia"]
    sinalex = False
    sinalpf = False
    """Retirando sinais(Frase está em String)"""
    if arg1.endswith("!"):
        arg1 = arg1.strip("!")
        sinalex = True
    if arg1.endswith("."):
        arg1 = arg1.strip(".")
        sinalpf = True
    """(String>>Lista)"""
    arg1 = arg1.split()
    """Censurando Palavrões"""
    for i in range(0, len(arg1)):
        for elemento in palavroes:
            if arg1[i] == elemento:
                arg1[i] = "*"*len(elemento)
    """(Lista>>String)"""
    frase_tratada = ' '.join(arg1)
    """Colocando sinais retirados"""
    if sinalex:
        frase_tratada = frase_tratada + "!"
    if sinalpf:
        frase_tratada = frase_tratada + "."
    return frase_tratada
frase = str(input())
frase_censurada = tratamento(frase)
print(frase_censurada)