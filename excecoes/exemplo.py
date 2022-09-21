# try e except
# Criar um programa que faça a divisão de dois números
# O programa deve validar a entrada de dados e somente
# números positivos


numero1 = input('Digite o 1° número: ')
numero2 = input('Digite o 2° número: ')

msg = ''


def validaNumero(n):
    try:
        global msg
        n = float(n)
        msg = msg + f'Número {n} foi convertido com sucesso!'
    except Exception as e:
        msg = msg + f'Não é possível converter {n} em float!{e}'

validaNumero(numero1)
validaNumero(numero2)
print(msg)
