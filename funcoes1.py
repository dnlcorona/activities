def palindromo (arg1):
    palavra_invertida = []
    for i in range(-1,-len(palavra)-1,-1):
        palavra_invertida.append(palavra[i])
    if (palavra == palavra_invertida):
        print("True")
    else:
        print("False")
    return palavra_invertida
palavra = list(input())
palindromo(palavra)