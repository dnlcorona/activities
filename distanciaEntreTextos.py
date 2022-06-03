"""
Faça uma função que receba como entrada dois dicionários contendo as frequências
das palavras em dois textos e retorne a soma da diferença absoluta entre as frequências
das palavras nos dois dicionários. Considere que algumas palavras podem existir no primeiro
texto, mas não aparecer no segundo e vice-versa. Por exemplo, considere os dois dicionários abaixo: 
d1 = {'agua': 3, 'casa': 5}
d2 = {'bola': 2, 'agua': 5}
As diferenças absolutas entre as frequências das palavras são: 
agua: 2    # abs(3 - 5)
casa: 5    # abs(0 - 5)
bola: 2     # abs(2 - 0)
Com isso, a função deveria retornar 2 + 5 + 2 = 9.
Use esta função e a função criada na parte 2 para construir um programa que leia dois textos
limpos e mostre na tela a soma das diferenças absolutas entre as frequências das palavras nos textos. 
Casos de Teste:
case=1
input=agua casa agua agua casa casa casa casa
bola agua agua agua agua agua bola
output=9
case=2
input=agua casa bola
item joia marcador codigo fonte
output=8
case=3
input=ola esse eh um teste
teste esse eh um ola
output=0
"""
def contador(arg1,arg2):
    dicio1 = {}
    dicio2 = {}
    lista1 = arg1.split()
    lista2 = arg2.split()
    sla = [lista1,lista2]
    for elemento in sla:
        for i in range(0,len(elemento)):
            contador = 0
            for j in range(0,len(elemento)):
                if elemento[i]==elemento[j]:
                    contador = contador + 1
                    if elemento == lista1:
                        dicio1[elemento[i]] = contador
                    else:
                        dicio2[elemento[i]] = contador
    return dicio1, dicio2
def diferencaabs(arg1):
    soma = 0
    somatotal = 0
    listasoma = []
    d1 = arg1[0]
    d2 = arg1[1]
    for chave in d1.keys():
        soma = 0
        for chave2 in d2.keys():
            if chave == chave2:
                soma = soma + abs(d1[chave]-d2[chave])
                listasoma.append(soma)
    for chavenotexist2 in d1.keys():
        if chavenotexist2 not in d2.keys():
            listasoma.append(d1[chavenotexist2])
    for chavenotexist1 in d2.keys():
        if chavenotexist1 not in d1.keys():
            listasoma.append(d2[chavenotexist1])
    for elemento in listasoma:
        somatotal = somatotal + elemento
    print(somatotal)
frase1 = str(input())
frase2 = str(input())
dicionarios = contador(frase1,frase2)
diferencaabs(dicionarios)