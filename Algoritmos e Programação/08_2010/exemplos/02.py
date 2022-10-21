##faça um alg que receba um numero e imprima a tabuada desse número.

a = int(input("Digite um número: "))
b = 0
print(f"A tabuada de {a} é: ")
while b < 10:
    b = b + 1
    print(f"{a}x{b}={a*b}")