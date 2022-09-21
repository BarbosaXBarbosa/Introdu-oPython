# 4 - Crie um fonte que leia dois números e pergunte ao usuário qual operação ele deseja fazer: Soma '+'
# Subtração '-', Multiplicação '*' ou Divisão '/'. Mostre o resultado da operação solicitada.

print('Bem vindo a calculadora podre!')
print()


def menu_operacao():
    operacao = int(input(
        'Qual operação você deseja fazer? \n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n  número da operação: '))
    return operacao


opcao = menu_operacao()

if opcao not in (1, 2, 3, 4):
    print('\nParâmetro Inválido!')
    print()
    menu_operacao()
else:
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))

    if n2 == 0:
        print("Não existe divisão por zero!")

    else:
        if opcao == 1:
            resultado = n1 + n2
            operador = '+'
        elif opcao == 2:
            resultado = n1 - n2
            operador = '-'
        elif opcao == 3:
            resultado = n1 * n2
            operador = '*'
        elif opcao == 4:
            resultado = n1 / n2
            operador: str = '/'

        # noinspection PyUnboundLocalVariable
        print(f'{n1:5.0f} {operador}{n2:5.0f} ={resultado:5.0f}')
