nfunc = int(input("Digite o número do funcionário "))
horastrab = float(input("Digite o número de horas trabalhadas: "))
vph = float(input("Digite o valor que o funcionário ganha por hora: R$"))
filhos = int(input("Digite quantos filhos com menos de 14 anos: "))
idade = int(input("Digite a idade do funcionário: "))
temp = float(input("Digite o tempo de serviço do funcionário: "))
salfilho = float(input("Digite o valor fixo de salario família por filho: R$"))

salbruto = horastrab * vph
salario = salbruto - (salbruto*0.085)
salftotal = filhos * salfilho
totaldesc = salbruto - salario
salliquid = salftotal + salario

print("O número do funcionário é: ",nfunc)
print("O salário bruto é: ",salbruto)
print("O total de descontos é: ",totaldesc)
print("O salário liquido é: ",salliquid)

if ((salbruto >= 1500) and (salbruto < 100000000000)):
    ir = salbruto * 0.15
    print("O imposto de renda é: R$",ir)
elif ((salbruto >= 500) and (salbruto <1500)):
    ir = salbruto * 0.08
    print("O imposto de renda é: R$",ir)
else:
    print("O empregado não paga imposto de renda.")
