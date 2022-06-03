from decimal import Decimal
"""a = "coe"
print(a[-3])
"""
"""
a = "3.998"
print(a[2])
"""
"""
print("3.00000000", 3.0000000)
"""
#STRINGS SAO IMUTÁVEIS
#PONTO FLUTUANTE
#TABELA
#print(-1**2)
#RESULTA EM ERRO:
"""
pi = 3.14159
pi2 = 3.14158
dif = (pi-3) - (pi2-3)
dif_formatada = "{0:.11f}".format(dif)
print(abs(float(dif_formatada)))
"""
"""
#TENTANDO SOLUCIONAR:
pi = 3.14159265358
pi2 = 3.14159265355
dif = Decimal(pi) - Decimal(pi2)
dif_formatada = "{0:.11f}".format(dif)
print(dif_formatada)
"""
nilaka = 3.0
valores_de_pi = []
valores_de_pi.append(3.00000000000)
for i in range(1,1501):
    somatoria = 0
    divisor = (((-1) ** (i+1)) * 4)
    dividendo = (2*i)*(2*i+1)*(2*i+2)
    somatoria += divisor/dividendo
    nilaka += somatoria         
    valores_de_pi.append(nilaka)

print(f"{valores_de_pi[1499]:.11f}")