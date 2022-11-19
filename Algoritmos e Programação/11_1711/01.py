moeda = str(input("Qual sua moeda atual: "))
valor = float(input("Qual o valor: "))
dolar = 5.42
if moeda == "dolar":
    conversao = valor*dolar
    print(f"A quantidade em reais é: {conversao:.2f}")
else:
    conversao = valor/dolar
    print(f"A quantidade em dolar é: {conversao:.2f}")