#Faça um algoritmo (FUA) que lê o número de um funcionário, seu número de horas
#trabalhadas e o valor que recebe por hora. O algoritmo deve calcular e mostrar o salário
#deste funcionário.

func = int(input("Digite o número do funcionario: "))
horatrab = int(input("Digite o número de horas trabalhadas: "))
valorhora = int(input("Digite o valor que o funcionario ganha por hora: "))

salario = horatrab*valorhora

print("O funcionario vai receber um total de R$",salario)