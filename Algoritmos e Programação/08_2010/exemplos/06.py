#Faça um programa que receba várias idades, calcule e mostre a média das idades digitadas. Finalize digitando idade igual a zero.

from operator import truediv

i = int(input("Digite uma idade: "))
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1