# 3 - Combustível

combustivel = input("Escolha qual tipo de combustível seu carro usa:\n'A'- Álcool \n'G'- Gasolina\n...")

if combustivel != ('A' or 'G'):
    print('Erro, parâmetro digitado é inválido')
else:
    print("Entendido")
    print()
    litros = int(input('Digite a quantidade de litros de combustivel que você quer reabastecer: '))
    if combustivel == 'A':
        valorPORlitro = 5
        if litros > 20:
            precoFinal = (valorPORlitro - (valorPORlitro * 0.05)) * litros
        else:
            precoFinal = (valorPORlitro - (valorPORlitro * 0.03)) * litros
    if combustivel == 'G':
        valorPORlitro = 2.90
        if litros > 20:
            precoFinal = (valorPORlitro - (valorPORlitro * 0.06)) * litros
        else:
            precoFinal = (valorPORlitro - (valorPORlitro * 0.04)) * litros
    # noinspection PyUnboundLocalVariable
    print(f'O preço do combustivel foi: R${precoFinal}')
