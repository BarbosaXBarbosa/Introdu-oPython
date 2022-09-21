import validacaoAtv2 as vl

# 2 - Faça um programa que primeiro receba três valores sem verificação
# nenhuma. Após as 3 entradas, o programa deve verificar através do
# try-except se os valores podem ser convertidos para int. Mostrar
# como resultado, para cada entrada de dados, se foi possível converter
# o valor para int ou não.

v1 = input('Digite o primeiro valor: ')
v2 = input('Digite o segundo valor: ')
v3 = input('Digite o terceiro valor: ')
vl.validaInteiro(v1)
vl.validaInteiro(v2)
vl.validaInteiro(v3)
