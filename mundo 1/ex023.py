""" Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Exemplo: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1

"""
from time import sleep
print('\033[1;31m*** Inicio do programa ***\033[m \n')

numero = eval(input('\033[1;36mInforme o número que deseja analisar: '))

if numero <= 9999:
    unidade = numero % 10
    dezena = (numero - unidade) // 10 % 10
    centena = (numero - dezena - unidade) // 100 % 10
    milhar = (numero - centena - dezena - unidade) // 1000 % 10
    print('Analisando o número {}...'.format(numero))
    sleep(2)
    print('\033[1;32mUnidade: {}'.format(unidade))
    print('\033[1;33mDezena:  {}'.format(dezena))
    print('\033[1;34mCentena: {}'.format(centena))
    print('\033[1;35mMilhar:  {}'.format(milhar))

else:
    print('\n \033[1;031mO número digitado não está no intervalo entre 0 e 9999!!!')
