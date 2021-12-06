# 10)- Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

C = float(input("Insira uma temperatura em Celsius: "))
F = (C * 9 / 5) + 32
print("%.1f °C é igual à %.1f °F" % (C, F))
