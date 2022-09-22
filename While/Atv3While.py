# 3 - Faça um programa que receba quantos números o usuário deseja digitar.
# O programa deve fazer a somatória de todos os números digitados e depois
# mostrar essa somatória na tela.

soma = 0
continuar = 's'
while continuar == 's':
    somador = int(input('Digite o número que você deseja somar: '))
    soma = soma + somador
    continuar = input('Você deseja continuar sua soma? \n'
          's: Sim \n'
          'n: Não\n'
          'R: ')
print(f'O valor da sua soma é: {soma}')