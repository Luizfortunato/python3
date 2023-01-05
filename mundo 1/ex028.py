""" Escreva um programa que faça o computador "pensar" em um número entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o utilizador venceu ou
perdeu.
"""

from random import randint
from time import sleep
print('\033[1;031m*** Início do jogo ***')

print('\033[1;033m------'*24)
print('\033[1;034mVou pensar em um número entre 0 e 5... Tente adivinhar :)')
print('\033[1;033m------'*24)

numero = int(input('\033[1;035mEm que número eu pensei: '))
aleatorio = randint(0, 5)

print('\033[1;033mProcessando...')
sleep(2)
if 0 <= numero <= 5:
    if numero == aleatorio:
        print('\033[1;032m\nVocê acertou eu pensei no numero {}'.format(aleatorio))

    else:
        print('\033[1;036m\nVocê errou!!! Eu pensei no número {}!!!'.format(aleatorio))

else:
    print('\033[1;031m\nNumero inválido!!! Digite um número entre 0 e 5')
