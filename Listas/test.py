# 1 - Faça um algoritmo de um caixa de super mercado. O algoritmo receberá n produtos,
# conforme o operador do caixa for inserindo. O programa receberá nome do produto,
# preço unitário e quantidade.
# Ao final o programa deve mostrar is itens comprados, preço unitário e preço total
# por item e o valor total da compra.


nome_produtos = []
preço_unitário = []
quantidade_produto = []
i = 0
quant = 0


while True:
    try:
        nome_produtos.append(input('Informe o nome do produto: '))
        if nome_produtos[i] == '0':
            nome_produtos.pop(i)
            print('Finalizando operação.')
            break
        else:
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
                quant += 1
    except Exception as e:
        if len(nome_produtos) != len(preço_unitário):
            print('Digite um preço válido!')
            nome_produtos.pop(i)
        elif len(preço_unitário) != len(quantidade_produto):
            print('Digite uma quantidade válida')
            nome_produtos.pop(i)
            preço_unitário.pop(i)
        print(e)
print('-' * 10 + 'Lista final' + '-' * 10 + '\n')

i = 0

total = 0
while True:
    total = total + (quantidade_produto[i] * preço_unitário[i])
    print(f'{quantidade_produto[i]} - {nome_produtos[i]}(s) custo: {quantidade_produto[i] * preço_unitário[i]}')
    i += 1
    if i == quant:
        break
final = '-' * 10 + 'Total:' + f'{total:5.2f}'
print(f'{final:>20}')
