num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
m1=0
m2=0
if ((num1 > num2)and(num1>num3)):
    m1 = num1
elif ((num2 > num1)and(num2 > num3)):
    m2 = num2
elif ((num3 > num1)and(num3 > num2)):
    m2 = num3

soma = m1 + m2
print(soma)