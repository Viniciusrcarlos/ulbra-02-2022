#F.U.A para calcular o valor de lucro que um vendedor tem em um produto, com base
#em seu preço de custo e o preço de venda.

from locale import LC_NUMERIC


custo = float(input("Digite o custo do produto em R$: "))
venda = float(input("Digite o preço de venda do produto em R$: "))

lucro = venda - custo

print("O lucro desse produto é: R$",lucro)