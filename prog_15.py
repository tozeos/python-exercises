# 15)- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# a)- salário bruto.
# b)- quanto pagou ao INSS.
# c)- quanto pagou ao sindicato
# d)- o salário líquido.

ganhoHora = int(input("Quanto tu ganha por hora: "))
horasTrabalhadasMes = float(input("Quantas horas trabalhastes neste mês: "))
salarioBruto = horasTrabalhadasMes * ganhoHora
IR = salarioBruto * 0.11
INSS = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = (salarioBruto - (IR + INSS + sindicato))

print("+ Salário Bruto: R$", salarioBruto)
print("- IR (11%): R$", IR)
print("- INSS (8%): R$", INSS)
print("- Sindicato (5%): R$", sindicato)
print("= Salário Líquido: R$", salarioLiquido)