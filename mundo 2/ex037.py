""" Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
— 1 para binário
— 2 para octal
— 3 para hexadecimal """

print('\033[1;31mConversor de bases numéricas')
numero = int(input('\n\033[33mDigite um número inteiro no qual deseja converte-lo: '))
print("""\033[34m\nInforme para qual base numérica deseja converter:
[1] Converter para binário.
[2] Converter para Octal.
[3] Converter para Hexadecimal.""")

escolha = int(input('\nDigite sua escolha: '))

if escolha == 1:
    print('\033[35mO número {} convertido em binário é {}'.format(numero, bin(numero)[2:]))

elif escolha == 2:
    print('\033[36mO número {} convertido em Octal é {}'.format(numero, oct(numero)[2:]))

elif escolha == 3:
    print('\033[33mO numero {} convertido em Hexadecimal é {}'.format(numero, hex(numero)[2:]))

else:
    print('\033[1;31m\nEscolha uma opção válida!!!')
