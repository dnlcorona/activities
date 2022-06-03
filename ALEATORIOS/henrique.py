"""
Henrique kpoper s2
      *-*
"""
from decimal import Decimal
def q2():
      zero = 0
      valores_de_pi = []
      valores_de_pi.append(3.00000000000)
      novos_valores_de_pi = []
      pi = 3.14159265358
      #difabslist = []
      nilaka = 3.0
      somatoria = 0
      pos_ponto = 0
      valor_limite = 1501
      for i in range(1,valor_limite):
            somatoria = 0
            divisor = (((-1) ** (i+1)) * 4)
            dividendo = (2*i)*(2*i+1)*(2*i+2)
            somatoria += divisor/dividendo
            nilaka += somatoria         
            valores_de_pi.append(nilaka)
      for numPi in valores_de_pi:
            for num in range(0,len(str(numPi))):
                  if str(numPi)[num] == ".":
                        pos_ponto = num
                        break
            for num in range(num+1,len(str(numPi))):
                  d = str(numPi)
                  antes_do_ponto = d[0:pos_ponto]
                  depois_do_ponto = d[pos_ponto:pos_ponto+12]
                  juntar = antes_do_ponto + depois_do_ponto
                  novos_valores_de_pi.append(juntar)  
                  break



      print("1 - Consulta pela quantidade de elementos da série de Nilakantha. \n" 
      "2 - Consulta pela precisão desejada."
      )
      escolha = int(input("Opção: "))


      pode = False
      pode2 = False
      while pode == False:
            if escolha == 1:
                  num_elem = int(input("Digite o número de elementos da série (1-1500): "))
                  if num_elem >= 1 and num_elem <=1500:                                           
                        print("Valor exato de PI com 11 casas decimais:    3.14159265358")
                        print(f"Valor de PI calculado com {num_elem: >4} elementos:   {novos_valores_de_pi[num_elem-1]}")
                        dif = abs(Decimal(pi) - Decimal(novos_valores_de_pi[num_elem-1]))
                        dif_formatada = "{0:.11f}".format(dif)
                        print(f"Módulo da diferença para valor exato de PI: {dif_formatada}")
                        pode = True
                        continue
                  else: 
                        print("Valor inválido!")
                        continue
            if escolha == 2:
                  while pode2 == False:
                        precisao = int(input("Precisão em casa decimais (1-10): "))
                        if precisao >=1 and precisao <=10:
                              print("Valor exato de PI com 11 casas decimais: 3.14159265358")
                              for idxNumPi in range(0,len(novos_valores_de_pi)):
                                    zero = 0
                                    dif = abs(Decimal(pi) - Decimal(novos_valores_de_pi[idxNumPi]))
                                    dif_formatada = "{0:.11f}".format(dif)
                                    for idx in range(2, precisao+2):
                                          if dif_formatada[idx] == "0":
                                                zero += 1
                                                continue
                                          else:
                                                break
                                    if zero == precisao: 
                                          break            
                                    continue
                              print(f"Valor de PI encontrado na posição {idxNumPi+1: >4}:  {novos_valores_de_pi[idxNumPi]}")
                              print(f"Módulo da diferença valor exato de PI:   {dif_formatada}")
                              pode2 = True
                              pode = True
                              continue
                        else:
                              print("Precisão deve ser entre 1 e 10")
                              pass
            else:
                  print("Opção inválida! Digite 1 ou 2!")
                  escolha = int(input("Opção: "))
                  continue
      continuar = str(input("Deseja continuar (S/n)?: "))
      if continuar == "S" or continuar == "s":
            q2()
      else: exit
print("Consulte o valor de PI, selecionando a opção abaixo! \n")
q2()
"""
def q1():
      #xereca
      #
      #
      espaco_vazio = ""
      passe1, passe2 = False, False
      listaDeNotas = []
      ListaDeNotasInt = []
      valor_min, valor_max, nota_min, nota_max = 2,20,0,100
      while passe1 == False:
            num_notas = int(input("Informe o número de notas: "))
            if num_notas < valor_min or num_notas > valor_max:
                  print(f"Valor deve estar entre {valor_min} e {valor_max}.")
                  passe1 = False
            else:
                  passe1 = True
      if passe1 == True:
            for _ in range(0,num_notas):
                  passe2 = False
                  while passe2 == False:
                        nota_momentanea = float(input(f"Nota {_+1}: "))
                        if nota_momentanea < 0 or nota_momentanea > 100:
                              print(f"Nota inválida! Valor deve estar entre {nota_min} e {nota_max}.")
                        else:
                              listaDeNotas.append(nota_momentanea)
                              passe2 = True
      for nota in listaDeNotas:
            resto = 0
            resto = nota - int(nota)
            resto = float("%.2f" % resto)
            if resto == 0:
                 nota = int(nota)
                 ListaDeNotasInt.append(nota) 
                 continue
            if resto < 0.5 and resto != 0:
                  nota = int(nota)
                  ListaDeNotasInt.append(nota)
                  continue
            else: 
                  nota = int(nota)
                  novaa_nota = nota + 1
                  ListaDeNotasInt.append(novaa_nota)
      print("Nota original", end="  ")
      print("Nota convertida")
      for _ in range(0,len(listaDeNotas)):
            print(f"{espaco_vazio: >4} {listaDeNotas[_]:.2f} {ListaDeNotasInt[_]: >14} {espaco_vazio}"
            )
      for nota in listaDeNotas:
            soma = 0
            soma = soma + nota
      for nota in ListaDeNotasInt:
            somaI = 0
            somaI = somaI + nota
      mediaI = somaI//len(ListaDeNotasInt) #deposi da conversao
      media = soma/len(listaDeNotas)
      #DESVIO PADRA
      desvio_padrao = []
      for idx in range(0,len(listaDeNotas)):
            desvio_padrao.append(((listaDeNotas[idx] - media)**2)/3.0)
      soma = 0
      for num in desvio_padrao:
            soma = soma + num
      total = soma ** 0.5
      print(f"Antes da conversão: Média = {media} Desvio Padrão = {total}")
      print(f"Antes da conversão: Média = {mediaI}")
q1()
"""
#LISTA >> ARRANJO
#PONTO FLUTUANTE