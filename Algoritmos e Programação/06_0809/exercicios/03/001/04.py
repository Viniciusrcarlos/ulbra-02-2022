#FUP que leia um número e mostre uma mensagem indicando se este número é par ou ímpar e se é positivo e negativo.

num = int(input("Digite um número: "))

impar=num%2

if impar == 0:
    print("O número é par")
else:
    print("O número é impar")

if num >= 0:
    print("O número é positivo")
else:
    print("O número é negativo")
