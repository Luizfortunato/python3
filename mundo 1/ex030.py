""" Crie um programa que leia um número inteiro e informe se ele é PAR ou ÍMPAR"""

numero = int(input('\033[1;33mMe diga um número qualquer? '))

if numero % 2 == 0:
    print('\033[1;34mO número {} é PAR!!!'.format(numero))
else:
    print('\033[1;35mO número {} é ÍMPAR!!!'.format(numero))
    