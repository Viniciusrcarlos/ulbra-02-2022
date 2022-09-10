#FUP para ler dois números. Se os números forem iguais, imprimir a mensagem:"numeros iguais" e encerrar a execução. caso contrário, imprimir o de maior valor.

num1 = int(input("Digite o número A: "))
num2 = int(input("Digite o número B: "))

if num1 == num2:
    print("Os números são iguais.")
elif num1 > num2:
    print(num1)
else:
    print(num2)
