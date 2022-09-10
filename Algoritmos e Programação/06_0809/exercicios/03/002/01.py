#Faça um programa que leia a altura e o sexo de uma pessoa, calcule seu peso ideal utilizando as seguintes formulas:
# * M: (72.7*altura)_58
# * F: (62.1*altura)-44.7
from re import M

sexo = str(input("Digite seu sexo, M para masculino e F para feminino: "))
altura = float(input("Digite sua altura: "))

if sexo == M:
    ideal=(72.7*altura)-58
    print(ideal)
else:
    ideal=(62.1*altura)-44.7
    print(ideal)
