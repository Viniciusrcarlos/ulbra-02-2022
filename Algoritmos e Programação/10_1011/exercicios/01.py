def imc():
    numero = []
    peso = []
    altura = []
    numero.append(float(input("Número do funcionário: ")))
    peso.append(float(input("Peso: ")))
    altura.append(float(input("Digite a altura do funcionário: ")))

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