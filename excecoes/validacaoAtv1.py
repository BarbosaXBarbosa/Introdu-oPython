# Validações da atividade 1
msg = ''


def validaPreco(preco):
    try:
        global msg
        preco = float(preco)
        if preco > 0:
            msg = f'preço: {preco} válido\n'
            print(msg)
    except Exception as e:
        msg = f'Preço: {preco} inválido! {e}\n'
        print(msg)
