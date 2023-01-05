""" Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que utilizando agora um laço for """

numero = int(input('\033[1;33mInforme o número que deseja saber a tabuada: '))
print('\033[1;32mSegue a tabuada do {}'.format(numero))
print('\033[1;34m=\033[1;35m'*20)

for C in range(1, 11):
    print('{} X {:2} = {:2}'.format(numero, C, numero*C))           # {:2} deixa todos os caracteres com 2 casas

print('\033[1;34m='*20)
