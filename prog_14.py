# 14)- João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
# trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
# São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa
# que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos
# além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as
# mensagens adequadas.

peso = float(input("Peso dos peixes: "))

if(peso > 50):
    excesso = peso - 50
    multa = excesso * 4
    print("Excesso: %.2f Kg" % excesso)
    print("Multa: R$ %.2f" % multa)
else:
    print("Você pescou %.2f Kg" % peso)
    print("21Se safou da multa!")

