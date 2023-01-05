""" Crie um programa que faça o computador jogar Jokenpô com o usuário """

from random import choice
from time import sleep
print('\033[1;35m{:^50}'.format('JO KEN PO !!!'))   # {:^50}Centraliza a palavra usando 50 espaços

print("""\033[34mSUAS OPÇÕES:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA """)

itens = ['PEDRA', 'PAPEL', 'TESOURA']                       # escolha do computador

computador = choice(itens)                                  # escolha do computador

escolha = int(input('\n\033[33mQual é a sua escolha? '))              # escolha jogador

if escolha == 1:
    jogador = 'PEDRA'

elif escolha == 2:
    jogador = 'PAPEL'

elif escolha == 3:
    jogador = 'TESOURA'

if escolha <= 3:

    print('\033[32mJO')
    sleep(0.7)
    print('\033[34mKEN')
    sleep(0.7)
    print('\033[35mPO !!!\n')
    sleep(0.4)

    print('\033[34mComputador escolheu \033[1;m{}'.format(computador))
    print('\033[34mJogador escolheu \033[1;m{}'.format(jogador))

    if jogador == 'PEDRA':
        if computador == 'PEDRA':
            print('\033[33mEmpate!!! ')

        elif computador == 'PAPEL':
            print('\033[33mCOMPUTADOR venceu!!!')

        elif computador == 'TESOURA':
            print('\033[32mJOGADOR venceu!!!')

    elif jogador == 'PAPEL':
        if computador == 'PEDRA':
            print('\033[32mJOGADOR venceu!!!')

        elif computador == 'PAPEL':
            print('\033[33mEmpate!!! ')

        elif computador == 'TESOURA':
            print('\033[33mCOMPUTADOR venceu!!!')

    elif jogador == 'TESOURA':

        if computador == 'PEDRA':
            print('\033[33mCOMPUTADOR venceu!!!')

        elif computador == 'PAPEL':
            print('\033[32mJOGADOR venceu!!!')

        elif computador == 'TESOURA':
            print('\033[33mEmpate!!! ')

else:
    print('\033[31mEscolha inválida!!!')
