veios_cinquenta_mais = 0
media_altura_idade_dez_a_vinte = []
pesoas_peso_inferior_a_quarenta = 0

for i in range(25): 
    altura = float(input("Digite a altura: "))   
    peso = float(input("Digite o peso: "))
    idade = int(input("Digite a idade: "))    
    if idade > 50:        
        veios_cinquenta_mais += 1    
    elif idade >= 10 and idade <= 20:        
        media_altura_idade_dez_a_vinte.append(altura)    
        if peso < 40:        pesoas_peso_inferior_a_quarenta += 1 

        print(f"A quantidade de pessoas com mais de 50 anos é {veios_cinquenta_mais}")
        print(f"A média de altura das pessoas com idade entre 10 e 20 anos é {sum(media_altura_idade_dez_a_vinte) / len(media_altura_idade_dez_a_vinte)}")
        print(f"A porcentagem de pessoas com peso inferior a 40 dentre todas as pessoas analisadas é {(pesoas_peso_inferior_a_quarenta / 25) * 100}%")