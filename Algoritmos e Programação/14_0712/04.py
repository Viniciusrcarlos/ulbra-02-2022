aguaMineral = 3
cafe = 7
chocolate = 5.5
paoDeQueijo = 5
qAgua = 0
qCafe = 0
qChoco = 0
qPao = 0
while True:
    qAgua=int(input('Quantidade de águas: '))
    qCafe=int(input('Quantidade de Cafe: '))
    qChoco=int(input('Quantidade de Chocolates: '))
    qPao=int(input('Quantidade de Pães de queijo: '))

    print('----------------***--------------')
    print(f'Quantidade de águas: {qAgua}')
    print(f'Preço por unidade: {aguaMineral}')
    print(f'Preço total das águas: {qAgua*aguaMineral}')
    print()
    print(f'Quantidade de Café: {qCafe}')
    print(f'Preço por unidade: {cafe}')
    print(f'Preço total do café: {qCafe*cafe}')
    print()
    print(f'Quantidade do Chocolate: {qChoco}')
    print(f'Preço por unidade: {chocolate}')
    print(f'Preço total do chocolate: {qChoco*chocolate}')
    print()
    print(f'Quantidade de Pães de quejo: {qPao}')
    print(f'Preço por unidade: {paoDeQueijo}')
    print(f'Preço total do café: {qPao*paoDeQueijo}')
    print()
    print(f'Total da venda: {(qAgua*aguaMineral)+(qCafe*cafe)+(qPao*paoDeQueijo)+(qChoco*chocolate)}')
    print('----------------***--------------')
    print()
    conf = str(input('Fazer nova venda? (S/N):  '))
    if conf == 's':
        continue
    elif conf == 'n':
        break