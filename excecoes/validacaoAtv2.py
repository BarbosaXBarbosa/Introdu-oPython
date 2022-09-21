def validaInteiro(v1):
    try:
        v1 = int(v1)
        print(f'O número: {v1} foi convertido com sucesso')
    except Exception as e:
        print(f'o valor: {v1}, não foi convertido corretamente. \n{e}')
