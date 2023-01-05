""" Crie um programa que leia o nome de uma cidade e diga se ela começa com a palavra 'Santo' """

print('\033[1;31m*** Início do programa ***\n\033[m')

cidade = str(input('\033[1;36mInforme o nome de uma cidade: \033[m')).strip().upper()
cidade = cidade.split()
print(cidade[0] == 'SANTO')

print('\n\033[1;031m*** Fim do programa ***')