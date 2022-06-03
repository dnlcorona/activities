def contador(arg1):
    dicio = {}
    lista = arg1.split()
    lista.sort()
    for i in range(0,len(lista)):
        contador = 0
        for j in range(0,len(lista)):
            if lista[i]==lista[j]:
                contador = contador + 1
                dicio[lista[i]] = contador
    for chave in dicio.keys():
        print(f'{chave}: {dicio[chave]}')
frase = str(input())
contador(frase)


"""



"""