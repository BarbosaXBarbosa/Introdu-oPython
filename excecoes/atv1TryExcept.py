import validacaoAtv1 as vl
# 1 - Faça um programa que pergunte o nome e o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato. O programa deve validar a entrada de dados através do try
# e o preço dos produtos deve ser sempre positivo.


nom = input('Digite o nome do produto escolhido: ')
p = input('Digite o preço do produto: ')
vl.validaPreco(p)

nom2 = input('Digite o nome do produto escolhido: ')
p2 = input('Digite o preço do produto: ')
vl.validaPreco(p2)

nom3 = input('Digite o nome do produto escolhido: ')
p3 = input('Digite o preço do produto: ')
vl.validaPreco(p3)

barato = p
prodb = nom
if p2 < barato:
    barato = p2
    prodb = nom2
if p3 < barato:
    barato = p3
    prodb = nom3

print(f'Produto recomendado: {prodb} \n'
      f'Valor: {barato} \n{vl.msg}')
