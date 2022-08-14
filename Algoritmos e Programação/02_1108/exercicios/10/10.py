#F.U.A que leia o preço de um produto e a quantidade comprada e exiba para o usuário
#o preço que ele tem que pagar pela compra.

preco = float(input("Digite o preço do produto comprado: R$"))
quantid = float(input("Digite a quantidade comprada: "))

total = preco * quantid

print("Você vai pagar um total de R$:",total)