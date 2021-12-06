# 9)- Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#     C = 5 * ((F-32) / 9).

F = float(input("Insira uma temperatura em Fahrenheit: "))
C = 5 * ((F - 32) / 9)
print("%.1f °F é igual à %.1f °C" % (F, C))
