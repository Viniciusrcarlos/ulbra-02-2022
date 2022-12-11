# Faça um algoritmo que receba Nome e as notas: AP1, AP2 e AS de pelo menos 20 alunos, após cada entrada
# de alunos, informe se ele aprovou ou reprovou e no final da digitação de todos os alunos da turma, 
# exiba um relatório com NOME de todos e sua APROVAÇÃO ou NÃO.

nome = []
ap1 = []
ap2 = []
aass = []
soma = []
i = 0
while i >= 0:
    nome.append(str(input('Digite o nome do aluno: ')))
    ap1.append(float(input('Digite a nota da AP1: ')))
    ap2.append(float(input('Digite a nota da AP2: ')))
    aass.append(float(input('Digite a nota da AS: ')))
    soma = ap1[i] + ap2[i] + aass[i]
    if soma >= 6:
        print('Aluno aprovado!')
        opcao = str(input('Deseja continuar? (S/N)'))
        if opcao == 's':
            i = i + 1
            continue
        elif opcao == 'n':
            break
                
    elif soma < 6:
        print('Aluno reprovado!')
        opcao = str(input('Deseja continuar? (S/N)'))
        if opcao == 's':
            continue
        elif opcao == 'n':
            break
i = 0
for x in nome:
    soma = ap1[i] + ap2[i] + aass[i]
    if soma >= 6:
        print('-----------***----------')
        print(f'Nome: {nome[i]}')
        print('Situação: Aprovado!!!')
        print('-----------***----------')
        print()
        i = i + 1
    elif soma < 6:
        print('-----------***----------')
        print(f'Nome: {nome[i]}')
        print('Situação: reprovado!!!')
        print('-----------***----------')
        print()
        i = i + 1