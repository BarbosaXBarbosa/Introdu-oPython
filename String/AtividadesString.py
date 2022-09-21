# 1 - Atribua seu nome completo a uma variável e mostre o 13° caractere do seu nome.
nome = 'João Victor Barbosa'

print(nome[12:13])

# 2 - Atribua seu nome completo a uma variável e capture o 3° caractere do seu nome e concatene com o 15° caractere
atividade = nome[2:3] + nome[14:15]
print(atividade)

# 3 - Multiplica por 50 os três primeiros caracteres do seu nome.
print(nome[0:3] * 50)

# 4 - Crie um fonte que receba um nome. Se o nome tiver mais de 6 caracteres, mostre na tela a seguinte informação
# 'nomeABCDEFXXX'. Se não mostre na tela: 'nome tem menos de 7 caracteres.'

name = input("Digite seu nome: ")
if len(name) > 6:
    print(f'{name} nomeABCDEFXXX')
else:
    print('nome tem menos de 7 caracteres')

# 5 - Mostre na tela a seguinte mensagem usando composições %s, %d e %f e variáveis:
# 'Juliano tem 1.72 de altura e pesa 00080 kilos.'

nm = 'Juliano'
altura = 1.72
peso = 80

print('%s tem %3.2f de altura e pesa %05d kilos' % (nm, altura, peso))

# 6 - Mostre a mesma mensagem anterior mais utilizando o '.format()' e o 'f-strings'
# (mostrar duas mensagens, uma para cada metodologia)

print('{} tem {} de altura e pesa {:05} kilos' .format(nm, altura, peso))
print(f'{nm} tem {altura} de altura e pesa {peso:05} kilos')

# 7 - Crie um fonte que receba o nome de uma cidade. Se o nome da cidade tiver 10 caracteres ou menos,
# o sistema deve informar: 'O nome da cidade de 'cidade' tem menos de 11 caracteres'. Se não deve informa:
# 'O nome da cidade de 'cidade' tem x caracteres'.

cidade = input("Informe o nome da cidade: ")

if len(cidade) <= 10:
    print(f'O nome da cidade de {cidade} tem menos de 11 caracteres.')
else:
    print(f'{cidade} tem {len(cidade)} caracteres')


# 8 - Crie um fonte que receba dois nomes de pessoas e verifique quais dos dois nomes
# tem a maior quantidade de caracteres. No final o sistema deve mostra: 'O nome 'nome' é maior'
# que o nome 'nome2'.

print('Saiba qual nome tem mais caracteres.')
print()
n1 = input('Insira um nome: ')
n2 = input('Insira o segundo nome: ')

if len(n1) > len(n2):
    print(f'O nome {n1} é maior que o nome {n2}.')
elif len(n1) == len(n2):
    print('Os nomes tem a mesma quantidade de caractér')
else:
    print(f'O nome {n2} é maior que o nome {n1}.')


# 9 - Crie um fonte que receba o nome de um estado brasileiro. O fonte deve pegar
# do 3 ao 7 caractere do nome e mostrá-lo na tela. O fonte deve verificar se o
# nome do estado digitado possui pelo menos 7 caracteres.

estado = input('Digite o nome do estado: ')

if len(estado) >= 7:
    print(f'{estado[3:7]}')
else:
    print('O nome do estado deve possuir pelo menos 7 caracteres.')


# 10 - Crie um fonte que receba seu nome completo. Crie para cada nome(sobrenome)
# variável separada e depois mostre cada nome e sobrenome em linhas diferentes.

nomeCompleto = input('Digite seu nome: ')

if nomeCompleto.find(" "):
    nome = nomeCompleto[0:nomeCompleto.index(" ")]
    sobrenome = nomeCompleto[nomeCompleto.index(" "):len(nomeCompleto)]
    print(f'Seu nome é :{nome} ')
    print(f'Seu sobrenome é: {sobrenome}')
else:
    print('Você deve colocar apenas o nome e sobrenome')
