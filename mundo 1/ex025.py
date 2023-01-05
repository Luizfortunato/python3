""" Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome """

print('\033[1;031m*** Início do programa ***\033[m\n')

nome = str(input('\033[1;032mInforme seu nome completo:')).strip().upper()
print('\033[1;033mSeu nome tem Silva? \033[1;036m{}'.format('SILVA' in nome))

print('\n\033[1;031m*** Fim do programa ***')
