# Crie um algoritmo que calcule a área de figuras geométricas planas(fórmulas informadas)
# que contenha um MENU para escolha de qual forma será calculada, utilize FUNÇÕES para a
# chamada das mesmas e uma interface adequada para sua utilização.
# Círculo: A = Pi.r2
# Quadrado: A = L2
# Retângulo: A = base.altura


# funcoes:
def funcaoCirculo():
    area = 3.14 * (raio ** 2)
    print('------------***-----------')
    print(f'Raio do Círculo: {raio}')
    print(f'Área do circulo: {area}')
    print('------------***-----------')


def funcaoQuadrado():
    area = lado ** 2
    print('------------***-----------')
    print(f'Lado do quadrado: {lado}')
    print(f'Área do quadrado: {area}')
    print('------------***-----------')


def funcaoRetangulo():
    area = base * altura
    print('------------***-----------')
    print(f'Base do Retângulo: {base}')
    print(f'Altura do Retângulo: {altura}')
    print(f'Área do retângulo: {area}')
    print('------------***-----------')


escolha = str(input("Digite o calculo que deseja fazer (Circulo, Quadrado ou Retângulo): "))
if escolha == 'circulo':
    raio = float(input('Digite o raio do círculo: '))
    funcaoCirculo()
elif escolha == 'quadrado':
    lado = float(input('Digite o tamanho do lado do quadrado: '))
    funcaoQuadrado()
elif escolha == 'retangulo':
    base = float(input('Digite a base do retângulo: '))
    altura = float(input('Digite a altura do retângulo: '))
    funcaoRetangulo()
