# 4 - Crie um programa que receba um valor inteiro e calcuke a sua tabuada,
# iniciando do 10 até o 0. O programa deverá também contar quantos números
# múltilplos de 3 serão gerados na tabuada. O usuário poderá digitar apenas
# valores entre -500 e 500. Validar entrada de dados com try-except.

while True:
    try:
        num = int(input('Digite um número entre -500 a 500 e faremos a sua tabuada: '))
        if num >= -500 and num <= 500:
            break
        else:
            print('O número deve estar entre -500 e 500 !!')
    except Exception as e:
        print(f'O {num} não foi convertido corretamente \n{e}')
i = 10
multiplos3 = 0
while i >= 0:
    result = num * i
    if result % 3 == 0:
        multiplos3 += 1
    print(f'{num} X {i} = {result}')
    i -= 1
print(f'\n{multiplos3} múltiplos de 3')



