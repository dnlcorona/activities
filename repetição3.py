palavra1 = str(input("Digite uma palavra: "))
palavra2 = str(input("Digite outra palavra: "))
boolean = False
if palavra1>palavra2:
    for i in range(0,len(palavra2)):
        if palavra1[i] == palavra2[i]:
            boolean = True
else:
    boolean = False
print(boolean)