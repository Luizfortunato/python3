""" O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
que leia o nome de quatro alunos e mostre uma ordem aleatória para a apresentação """
from random import shuffle
print('*** Início do programa ***\n')

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]

shuffle(lista)
print('A ordem de apresentação do trabalho será:')
print(lista)
print('\n*** FIm do programa ***')
