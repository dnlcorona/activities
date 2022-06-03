def limpezastring(arg1):
    for letra in arg1:
        if letra.isalpha() == False:
            arg1 = arg1.replace(letra," ")
    print(arg1)
frase = input()
limpezastring(frase)