palavra = str(input("Digite uma palavra: "))
letra = str(input("Digite a letra que você deseja contar: "))
contador = 0
for i in range(0,len(palavra)):
    if palavra[i] == letra:
        contador = contador + 1
print(f"A LETRA {letra} FOI ENCONTRADA {contador} VEZES NA PALAVRA {palavra}")