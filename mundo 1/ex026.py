""" Faça um programa que leia uma frase do teclado e mostre:
— Quantas vezes aparece a letra 'A'
— Em que posição ela aparece a primeira vez
— Em que posição ela aparece a última vez
"""

print('\033[1;031m*** Início do programa *** \n')

frase = str(input('\033[1;032mDigite uma frase para ser analisada: ')).strip().upper()
print('\033[1;036mA letra A aparece {} vezes na sua frase.'.format(frase.count('A')))

frase = frase.replace(' ', '') # retirando os espaços da frase

print('\033[1;034mA letra A aparece a primeira vez na posição {} da frase'.format(frase.find('A') + 1))

print("\033[1;035mA última vez que a letra A apareceu na frase foi na poição {}.".format(frase.rfind('A') + 1))

print('\n\033[1;31m*** Fim do programa ***')
