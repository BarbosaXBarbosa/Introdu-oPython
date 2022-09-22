# 2 - Faça um programa que imprima 20 vezes na tela a palavra 'Oi' mais o número da
# repetição que está ocorrendo
import time

i = 1
while i <= 20:
    print(f'{i}° Oi')
    time.sleep(0.5)
    i += 1
