# 11) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo

num1 = int(input("Mim dê um número: "))
num2 = int(input("Mim dê outro número: "))
num3 = float(input("Mim dê mais um número: "))

print("O produto do dobro do primeiro com metade do segundo:", (num1 * 2) * (num2 / 2))
print("A soma do triplo do primeiro com o terceiro:", (num1 * 3) + num3)
print("O terceiro elevado ao cubo:", pow(num3, 3))
