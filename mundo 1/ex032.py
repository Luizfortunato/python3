""" Faça um programa que leia um ano qualquer e mostre se ele foi é ou será bissexto. """

from datetime import date                               # importando a data da função datetime

ano = int(input('\033[1;34mInforme um ano qualquer ou digite zero para o ano atual: '))

if ano == 0:
    ano = date.today().year                             # utilizando apenas o ano da função data atual

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0):
    print('\033[1;35mO ano {} é um ano Bissexto!!!'.format(ano))

else:
    print('\033[1;36mO ano {} não é Bissexto!!!'.format(ano))
