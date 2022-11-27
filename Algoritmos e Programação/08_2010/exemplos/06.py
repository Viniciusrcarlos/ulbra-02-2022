#Faça um programa que receba várias idades, calcule e mostre a média das idades digitadas. Finalize digitando idade igual a zero.

idades = []
i = 0
while True:
  idades.append(int(input('Digite uma idade: ')))
  verif = str(input('Continuar? s/n    '))
  if verif == 's':
    continue
  elif verif == 'n':
    print(f'Quantidade de idades coletadas: {len(idades)}')
    print(f'A média das idades coletadas é: {sum(idades)/len(idades)}')



