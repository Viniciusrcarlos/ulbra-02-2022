#Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = []
i = 1
for x in range (5):
    numeros.append(float(input(f'Digite o {i}˚ número: ')))
    i = i+1

soma = sum(numeros)
media = sum(numeros)/len(numeros)
print(f'A soma dos números digitados é: {soma}')
print(f'A media dos números digitados é: {media}')
