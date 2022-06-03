nomeUsuario = str(input("Digite seu nome: "))

valorSalario = int(input("Digite seu salário: "))

inss = valorSalario * 0.05
previdencia = valorSalario * 0.02
salarioLiquido = valorSalario - inss - previdencia
print(f"Ola {nomeUsuario}, seguem as informações:")

print(f"Contribuição de INSS: {inss}")

print(f"Contribuição de previdência privada: {previdencia}")
print(f"Salário líquido: {salarioLiquido} reais")