#Envio da Resposta do TDE - *Faça um programa que leia um valor inteiro (que representa o real, moeda nacional) e calcule
#qual o menor número possível de notas/moedas de 100, 50, 20, 10, 5, 2 e 1 em que o valor lido
#pode ser decomposto. Escrever o valor lido e a relação de notas necessárias.*

numero = int(input("Digite o valor em R$: R$"))

cem = int(numero / 100)
numero = numero % 100
    
cinquenta = int(numero/50)
numero = numero % 50

dez = int(numero/10)
numero = numero % 10

cinco = int(numero/5)
numero = numero % 5

um = numero
    
print('Notas R$100,00 = ',cem)
print('Notas R$ 50,00 = ',cinquenta)
print('Notas R$ 10,00 = ',dez)
print('Notas R$  5,00 = ',cinco)
print('Notas R$  1,00 = ',um)