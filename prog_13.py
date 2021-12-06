# 13)- Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7h) - 58
# Para mulheres: (62.1h) - 44.7

h = float(input("Insira uma altura: "))
homem = (72.7 * h) - 58
mulher = (62.1 * h) - 44.7

print("Se for homem, seu peso ideal é: %.2fkg" % homem)
print("Se for mulher, seu peso ideal é: %.2fkg" % mulher)
