# Crie um programa que leia algo do teclado e mostre na tela o seu tipo primitivo e
# todas as informações possíveis sobre ele.

print('Inicio do programa!!!\n')

dado = input('\nDigite algo: ')

print('\nQual o tipo primitivo do valor? {}'.format(type(dado)))

print('\nEle é composto apenas de espaços? {}'.format(dado.isspace()))

print('\nEle é numérico? {}'.format(dado.isnumeric()))

print('\nEle é contém apenas letras? {}' .format(dado.isalpha()))

print('\nEle é alfanumérico? {}'.format(dado.isalnum()))

print('\nEstá completamente em letras maiusculas? {}' .format(dado.isupper()))

print('\nEsta completamente em letras minusculas? {}' .format(dado.islower()))

print('\nEstá capitalizado (Primeira letra maiuscula?)? {}' .format(dado.istitle())) # capitalizado é o termo que se usa no caso da primeira letra da palavra ser maiuscula.

print('\n\nFim do programa!!!')
