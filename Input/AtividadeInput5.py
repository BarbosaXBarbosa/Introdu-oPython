# 5 - Crie um fonte para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade
# de anos a pagar. O valor da prestação mensal não pode pode ser superior a 30%
# do salário. Calcule o valor da pretação como sendo o valor da casa a comprar
# dividido pelo número de meses a pagar. O programa deve informar ao usuário se
# empréstimo foi aprovado ou não. Em amobos os casos deve mostrar o valor da mensalidade.

print('Digite suas informações e descobriremos se seu empréstimo pode ser aprovado ou não')
print()

valorCasa = int(input('Digite o valor da casa escolhida: '))
salario = int(input('Digite qual é seu salário: '))
qtdAnos = int(input('Digite a quantidade de anos à pagar a casa: '))

mesesPagar = 12 * qtdAnos
valorPrestacao = valorCasa / mesesPagar
if valorPrestacao > (salario * 0.3):
    print('Seu empréstimo não foi aprovado!')
else:
    print(f'Parabéns seu empréstimo foi aprovado!\nSuas parcelas vão ser de R${valorPrestacao} por mês')
