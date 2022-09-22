# 1 - Faça um programa que receba um nome de foguete e gere uma contagem regressiva para seu lançamento.
# A contagem deve inciiar em 10 e finalizar em 1 e logo em seguida o programa deve imprimir na tela:
# "Lançamento do foguete{nome} iniciado!". Usar time.sleep(1)
import time

foguete = input("Diga o nome do foguete: ")

i = 10
print(f'Lançamento do {foguete} em:\n')
while i >= 0:
    print(f'{i}')
    time.sleep(1)
    i -= 1

