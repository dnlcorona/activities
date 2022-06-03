def rendimentos (arg1,arg2,arg3):
    rendimento = (arg1 * ((1 + arg2) ** arg3)) - arg1
    print("%.2f" % rendimento)
montante_investido = int(input())
taxa_retorno = float(input())
meses = int(input())
rendimentos(montante_investido,taxa_retorno,meses)