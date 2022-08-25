#Crie um algoritmo que leia dois valores numéricos e a partir disso faça para cada um deles (primeiro e segundo números):
#(1) se o valor for par:
#--------Imprima na tela a frase O Número digitado é par. ok
#(2) se o valor for ímpar:
#--------Imprima na tela a frase O Número digitado é ímpar. ok
#(3) se o número for menor que 10:
#--------Imprima na tela a frase O Número é menor que 10.ok
#(4) se o número for maior que 10:
#--------Imprima na tela a frase O Número é maior que 10.ok
#(5) imprima na tela o quadrado de cada número:
#(6) imprima na tela o resto da divisão de cada número por 2:
#(7) imprima na tela a soma dos dois números;
#Instrução: O Algoritmo deve primeiramente receber as duas entradas e após imprimir na tela as solicitações na ordem proposta.

from traceback import print_tb
#teste

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segunda número: "))


#par ou impar
if (num1%2) == 0:
    print("O primeiro número é par")
else:
    print("O primeiro número é ímpar")
if (num2%2) == 0:
    print("O segundo número é par")
else:
    print("O segundo número é ímpar")


#maior ou menor que 10
if (num1>10):
    print("O primeiro número é maior que 10.")
else:
    print("O primeiro número é menor que 10.")
if (num2>10):
    print("O segundo número é maior que 10.")
else:
    print("O segundo número é menor que 10.")