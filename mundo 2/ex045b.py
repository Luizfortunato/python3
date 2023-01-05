""" Crie um programa que faça o computador jogar Jokenpô com o usuário """
from random import randint
from time import sleep
print('{:^40}'.format('\33[11;34m JO KEN PO '))

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)                                      # escolha do computador

print("""SUAS OPÇÕES
[ 1 ] PEDRA 
[ 2 ] PAPEL
[ 3 ] TESOURA""")

jogador = int(input('Qual é a sua jogada? '))                  # escolha do jogador
if jogador > 2:
    print('Jogada inválida!!!')

else:
    print('JO')
    sleep(0.7)
    print('KEN')
    sleep(0.7)
    print('PO!!!')
    sleep(0.5)
    print('A escolha do computador foi {}'.format(itens[computador]))
    print('A escolha do jogador foi {}'.format(itens[jogador]))

    if computador == 0:
        if jogador == 0:
            print('EMPATE!!!')

        elif jogador == 1:
            print('VITÓRIA do JOGADOR!!!')

        elif jogador == 2:
            print('VITÓRIA do COMPUATDOR!!!')

    elif computador == 1:
        if jogador == 0:
            print('VITÓRIA do COMPUTADOR!!!')

        elif jogador == 1:
            print('EMPATE!!!')

        elif jogador == 2:
            print('VITÓRIA do JOGADOR!!!')

    elif computador == 2:
        if jogador == 0:
            print('VITÓRIA do JOGADOR!!!')

        elif jogador == 1:
            print('VITÓRIA do COMPUTADOR!!!')

        elif jogador == 2:
            print('EMPATE!!!')
