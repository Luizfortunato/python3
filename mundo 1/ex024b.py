""" Crie um programa que leia o nome de uma cidade e diga se ela começa com a palavra 'Santo'
Realizado de uma forma diferente.
"""
print('\033[1;031m*** Início do programa ***\033[m')

cidade = str(input('\033[1;33m\nInforme o nome de uma cidade: \033[1;35m')).strip().upper()
print(cidade[0:5] == 'SANTO') # compara se as primeiras 5 letras da palavra digitada é = a SANTO.

print('\033[1;31m\n*** Fim do programa ***')
