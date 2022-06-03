numero = int(input("Digite o tamanho que a lista terá: "))
L = []
for i in range(numero):
    numeroinserir = int(input("Digite um número para inserir na lista: "))
    L.insert(i,numeroinserir)
    
soma = 0
for i in range(len(L)):
    soma = soma + L[i]



menor = L[0]
for m in L:
    if m < menor:
        menor = m


for d in range(0,numero,1):
    if L[d] == menor:
        indice = d

print(f"{indice} {menor} {soma}")
