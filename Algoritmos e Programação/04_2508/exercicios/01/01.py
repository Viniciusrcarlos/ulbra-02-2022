#Crie um algoritmo que leia dois valores numéricos e a partir disso faça para cada um deles (primeiro e segundo números):
#(1) se o valor for par:
#--------Imprima na tela a frase O Número digitado é par. ok
#(2) se o valor for ímpar:
#--------Imprima na tela a frase O Número digitado é ímpar. ok
#(3) se o número for menor que 10:
#--------Imprima na tela a frase O Número é menor que 10.ok
#(4) se o número for maior que 10:
#--------Imprima na tela a frase O Número é maior que 10.ok
#(5) imprima na tela o quadrado de cada número: ok
#(6) imprima na tela o resto da divisão de cada número por 2: ok
#(7) imprima na tela a soma dos dois números; ok
#Instrução: O Algoritmo deve primeiramente receber as duas entradas e após imprimir na tela as solicitações na ordem proposta.


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segunda número: "))


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

#quadrado do número

num1quad = num1 * num1
num2quad = num2 * num2

print("O quadrado do primeiro número é: ",num1quad)
print("O quadrado do segundo número é: ",num2quad)

#resto da divisão por 2

num1restdiv = num1 % 2
num2restdiv = num2 % 2

print("O resto da divisão do primeiro número por 2 é: ",num1restdiv)
print("O resto da divisão do segundo número por 2 é: ",num2restdiv)

#soma dos dois números

soma = num1+num2

print("A soma entre os dois números é: ",soma)