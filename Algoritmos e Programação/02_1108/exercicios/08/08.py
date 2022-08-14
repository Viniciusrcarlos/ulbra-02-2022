#Uma loja de animais precisa de um algoritmo para calcular os custos de criação de
#coelhos. O custo é calculado com a fórmula CUSTO=(NRO_COELHOS*0.70)/18+10. O
#algoritmo tem como entrada o número de coelhos, devendo fornecer, como saída, o custo.

coelhos = float(input("Digite q quantidade de coelhos na loja: "))

custo = (coelhos*0.70)/18+10

print("O Custo de criação dos coelhos é: R$",custo)