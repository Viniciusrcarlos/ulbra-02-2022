#Crie um algoritmo que receba o nome, sexo, idade e tempo de trabalho (contribuição).
#Com base nos seguintes requisitos para aposentadoria: 
#Mulheres - 30 anos de contribuição e 55 anos de idade
#Homens - 35 anos de contribuição e 60 anos
#Diga se as pessoas consultadas podem ou não requerer a aposentadoria.
#Armazene as informações consultadas em uma lista e informe no final um relatório de consultas.
#Necessário MENU com interface para usuário (no termial, não é tela gráfica!).

nome = []
sexo = []
idade = []
tempoDeTrabalho = []

while True:
    nome.append(str(input("Nome: ")))
    sexo.append(str(input("Sexo: (M/F)")))
    idade.append(int(input("Idade: ")))
    tempoDeTrabalho.append(float(input("Tempo de trabalho em anos: ")))
    escolha = str(input("Cadastrar mais uma pessoa? (S/N)"))
    if escolha == "s":
        continue
    elif escolha == "n":
        break

i = 0
for x in nome:
    if sexo[i] == "m":
        if idade[i] >= 60 and tempoDeTrabalho[i] >= 35:
            print("------------***-----------")
            print(f"Nome: {nome[i]}")
            print(f"Sexo: {sexo[i]}")
            print(f"Idade: {idade[i]}")
            print(f"Tempo de trabalho: {tempoDeTrabalho[i]}")
            print("Apto a aposentadoria: Sim!")
            print("------------***-----------")
        else:
            print("------------***-----------")
            print(f"Nome: {nome[i]}")
            print(f"Sexo: {sexo[i]}")
            print(f"Idade: {idade[i]}")
            print(f"Tempo de trabalho: {tempoDeTrabalho[i]}")
            print("Apto a aposentadoria: Não!")
            print("------------***-----------")
    elif sexo[i] == "f":
        if idade[i] >= 55 and tempoDeTrabalho[i] >= 30:
            print("------------***-----------")
            print(f"Nome: {nome[i]}")
            print(f"Sexo: {sexo[i]}")
            print(f"Idade: {idade[i]}")
            print(f"Tempo de trabalho: {tempoDeTrabalho[i]}")
            print("Apto a aposentadoria: Sim!")
            print("------------***-----------")
        else:
            print("------------***-----------")
            print(f"Nome: {nome[i]}")
            print(f"Sexo: {sexo[i]}")
            print(f"Idade: {idade[i]}")
            print(f"Tempo de trabalho: {tempoDeTrabalho[i]}")
            print("Apto a aposentadoria: Não!")
            print("------------***-----------")
    i = i + 1