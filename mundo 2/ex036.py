""" Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa deve perguntar o valor
do imóvel, o salário do comprador e em quantos anos ele deseja pagar. Calcule o valor da prestação mensal, sabendo que
ela não pode exceder 30% do salário ou então o empréstimo será negado. """
from math import ceil
print('\033[1;32m=-='*40)
print('\033[1;31m PROGRAMA CASA PARA TODOS!!!')
print('\033[1;32m=-='*40)

nome = str(input('\n\033[1;34mQual o nome do cliente? '))
salario = eval(input('Informe o valor do salário mensal: R$ '))
valor = eval(input('Qual o valor do imóvel a ser financiado: R$ '))
prazo = int(input('Qual o prazo em anos deseja pagar o empréstimo? ')) * 12
mensalidade = (valor / prazo)

if mensalidade <= (salario * 30/100):
    print('\033[1;035m\nParabéns {} o seu financiamento foi aprovado!!!'.format(nome))
    print('O valor da sua prestação é de R$ {:.2f}'.format(mensalidade))
    print('Você deverá pagar esse valor por {} meses ou {:.0f} anos!!!'.format(prazo, prazo/12))

else:
    print('\033[1;31m\nDesculpe {} o seu financiamento não foi aprovado!!!'.format(nome))
    print('O valor máximo das suas prestações deve ser de até 30% de sua renda ou R${:.2f}'.format(salario * 30/100))
    prazo = (valor / (salario * 30/100))
    print('Aumente o prazo para {:.0f} anos ou {:.0f} meses'.format(ceil(prazo/12), prazo))
