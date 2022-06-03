
num = int(input("Digite o tamanho da lista desejada: "))
lst = []

contagem = 1
while contagem <= num :
    nome = input("Digite algo para que seja adicionada a lista:")
    lst.insert(contagem-1, nome)
    contagem = contagem + 1
print(lst)


'''
L = ["1", "2", "1", "agua", "bbb", "agua", "agua", "2", 1, 2, "1"]
valor = input("Digite o valor que deseja contar qnts vezes apareceu na lista: ")
input(f" O valor {valor} apareceu {L.count(valor)} vezes na lista")
'''






