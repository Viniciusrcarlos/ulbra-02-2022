def imc():
    lista = []
    lista.insert(0, float(input("peso: ")))
    lista.insert(1, float(input("altura: ")))

    imc = lista[0] / lista[1]**2

    if imc < 16:
        print("Magreza grave")
    elif imc < 17:
        print("Magreza moderada")
    elif imc < 18.5:
        print("Magreza leve")
    elif imc < 25:
        print("Saudável")
    elif imc < 30:
        print("Sobrepeso")
    elif imc < 35:
        print("Obesidade Grau I")
    elif imc < 40:
        print("Obesidade Grau II (severa)")
    else:
        print("Obesidade Grau III (mórbida)")

i = 0
while i < 9999:
    i = i + 1
    imc()
    resposta = str(input("Continuar? s=sim n=não: "))
    if resposta == "n":
        break
    elif resposta == "s":
        continue