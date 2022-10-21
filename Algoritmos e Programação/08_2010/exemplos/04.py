##Faça um programa que mostre as tabuadas dos números de 1 a 10

a = 0
while a < 10:
    a = a + 1
    b = 0
    print(f"A tabuada de {a} é: ")
    while b < 10:
        b = b + 1
        print(f"{a}x{b}={a*b}")