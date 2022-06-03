def tratamento (seq1, seq2):
    lista1, lista2 = seq1.split(), seq2.split()
    lista1float, lista2float = [], []
    for elemento in lista1:
        lista1float.append(float(elemento))
    for elemento in lista2:
        lista2float.append(float(elemento))
    return lista1float,lista2float
def prodinterno (arg1, arg2):
    mult = []
    soma = 0.0
    for i in range(0, len(arg1)):
        mult.append(arg1[i] * arg2[i])
    for o in range(0, len(arg1)):
        soma = soma + mult[o]
    print(int(soma))
sequencia1, sequencia2 = str(input()), str(input())
listas = tratamento(sequencia1, sequencia2)
lista1float = listas[0]
lista2float = listas[1]
prodinterno(lista1float, lista2float)