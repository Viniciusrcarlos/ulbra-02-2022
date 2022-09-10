#FUP para ler dois valores núméricos e apresentar a diferença do maior pelo menor.

num1 = int(input("Digite o número A: "))
num2 = int(input("Digite o número B: "))

if num1 > num2:
    num3=num1-num2
    print("A diferença entre o maior e o menor é:",num3)
else:
    num3=num2-num1
    print("A diferença entre o maior e o menor é:",num3)
