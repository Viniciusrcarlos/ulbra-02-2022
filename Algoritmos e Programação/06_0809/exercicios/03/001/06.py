#Ler 3 números;
#Se o primeiro for positivo, imprimir sua raiz quadrada, caso contrário, imprimir o seu quadrado.
#se o segundo numero for maior que 10 e menor que 100 imprimir "numero está entre 10 e 100 - intervalo permitido"
#se o terceiro for menor que o segundo escrever a diferença entre eles , caso contrario escrever a soma entre eles.

import math

num1 = int(input("Digite o número A: "))
num2 = int(input("Digite o número B: "))
num3 = int(input("Digite o número C: "))

if num1 >= 0:
    print(math.sqrt(num1))
elif num1 < 0:
    quad=num1*num1
    print(quad)
elif ((num2 >= 10) and (num2 <= 100)):
    print("Número está entre 10 e 100 - Intervalo permitido")
