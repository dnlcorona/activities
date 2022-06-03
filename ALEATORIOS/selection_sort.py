import timeit
import random as rd

#Cria a Lista
lista = []
tamanhoLista = 100
for numero in range(0,tamanhoLista):
    lista.append(numero)

#Complexidade O(n^2)
def selection_sort(l):
    for i in range(len(l)):
        min_idx = i
        for j in range(i+1, len(l)):
            if l[j] < l[min_idx]:
                min_idx = j
        aux = l[i]
        l[i] = l[min_idx]
        l[min_idx] = aux

tempos = []
somaTempos = 0
mediaDeTempo = 10
for i in range(mediaDeTempo):
    rd.shuffle(lista)#Embaralhar a lista
    startTime = timeit.default_timer()
    selection_sort(lista)
    finalTime = timeit.default_timer()
    tempos.append(finalTime - startTime)
    print(finalTime - startTime)
for i in tempos:
    somaTempos = somaTempos + i
media = somaTempos/mediaDeTempo
print(f"Selection Sort: {media}")


