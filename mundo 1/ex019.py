''' Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
nome deles e escrevendo o nome do escolhido.'''
from random import choice

print('*** Inicio do programa ***\n')

nome1 = str(input('Digite o nome do primeiro aluno: '))
nome2 = str(input('Digite o nome do segundo aluno: '))
nome3 = str(input('Digite o nome do terceiro aluno: '))
nome4 = str(input('Digite o nome do quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print('\nO aluno escolhido foi {}!!!'.format(escolhido))
print('\n*** Fim do programa ***')
