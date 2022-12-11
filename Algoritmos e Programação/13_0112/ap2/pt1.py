lista_pessoas = []

while True:
    pessoa = []
    pessoa.append(input("Digite seu Nome: "))
    pessoa.append(input("Digite o seu cgu: "))
    pessoa.append(input("Digite o seu email: "))
    lista_pessoas.append(pessoa)
    escolha = input("\nAdicionar outra pessoa? (S/N): ").upper().strip()

    if escolha ==  "N":
            break

for i in lista_pessoas:
    print(f"Nome: {i[0]} - CGU: {i[1]} - Email: {i[2]}")