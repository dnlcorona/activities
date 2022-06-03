palavra1 = str(input("Digite uma palavra: "))
palavra2 = str(input("Digite outra palavra com a mesma quantidade de letras: "))
contador = 0

for i in range(0,len(palavra1)):
    if palavra1[i] == palavra2[i]:
        contador = contador + 1

print(contador)
