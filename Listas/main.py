# Cria um programa que receba o nome de 10 alunos e suas respectivas medias finais
# No final o programa debe exibir a media de notas dos alunos e quantos alunos
# foram aprovados

nome_alunos = []
media_alunos = []  # lista das médias dos alunos
media_total = 0  # acumuladora das notas
contA = 0  # Contador de Aprovados
quant = 3
i = 0  # contador

while True:
    try:
        nome_alunos.append(input(f'Digite o nome do {i+1}º aluno: '))
        media_alunos.append(float(input(f'Digite a média do {nome_alunos[i]}: ')))
        if 0 < media_alunos[i] > 10:
            nome_alunos.pop(i)
            media_alunos.pop(i)
            print('Valor inváildo! Digite um número entre 0 e 10')
        else:
            media_total += media_alunos[i]
            if media_alunos[i] >= 7:
                contA += 1
            i += 1
            if i == quant:
                break
    except Exception as e:
        nome_alunos.pop(i)
        print('Erro! Digite o valor corretamente.')
        print(e)
print('-' * 10 + 'Indicadores finais' + '-' * 10 + '\n')
media_total = (media_total/len(nome_alunos))
print(f'Média dos alunos: {media_total:.2f}')
print(f'Quantidade de alunos aprovados: {contA}')
