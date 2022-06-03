def kmenores(arg1, arg2):
    contador = []
    lista = arg2.split()
    for idx in range(0,len(lista)):
        if arg1>int(lista[idx]):
            contador.append(idx)
    print(contador)
k = int(input())
numeros = str(input())
kmenores(k,numeros)

