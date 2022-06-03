cont = 0
pos_ponto = 0
x = 0
a = float(input("Digite um numero float: "))

#MÉTODO 1
b = "{0:.2f}".format(a)
#MÉTODO 2
c = round(a,2)
#MÉTODO 3
for num in range(0,len(str(a))):
    if str(a)[num] == ".":
        pos_ponto = num
        break
for num in range(num+1,len(str(a))):
    cont += 1
x = cont - 2
d = str(a)
antes_do_ponto = d[0:pos_ponto]
depois_do_ponto = d[pos_ponto:pos_ponto+3]
juntar = antes_do_ponto + depois_do_ponto
print(b, c, juntar)
