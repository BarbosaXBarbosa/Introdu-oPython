# 1 - Faça um algoritmo de um caixa de super mercado. O algoritmo receberá n produtos,
# conforme o operador do caixa for inserindo. O programa receberá nome do produto,
# preço unitário e quantidade.
# Ao final o programa deve mostrar is itens comprados, preço unitário e preço total
# por item e o valor total da compra.


nome_produtos = []
preço_unitário = []
quantidade_produto = []
quant = 0

while True:
    try:
        quant = int(input('Informe a quantidade dos produtos que você vai comprar: '))
        if 0 > quant or quant > 50:
            print('Excedeu o limite de volume de compras!')
        else:
            break
    except Exception as err:
        print('Erro! Quantidade inválida!')
        print(err)

i = 0

while True:
    try:
        nome_produtos.append(input('Informe o nome do produto: '))
        preço_unitário.append(float(input('Informe o preço deste produto: ')))
        if 0 > preço_unitário[i] or preço_unitário[i] > 500:
            preço_unitário.pop(i)
            nome_produtos.pop(i)
            print('Preço Inválido!')
        else:
            quantidade_produto.append(int(input(f'Informe a quantidade que você deseja de {nome_produtos[i]}: ')))
            if quantidade_produto[i] < 0 or quantidade_produto[i] > 20:
                print('Quantidade Inválida de produtos!')
            i += 1
            if i == quant:
                break
    except Exception as e:
        nome_produtos.pop(i)
        print('Erro! Digite o valor corretamente.')
        print(e)

print('-' * 10 + 'Lista final' + '-' * 10 + '\n')

i = 0

while True:
    print(f'{quantidade_produto[i]} - {nome_produtos[i]}(s) total: {quantidade_produto[i] * preço_unitário[i]}')
    i += 1
    if i == quant:
        break
