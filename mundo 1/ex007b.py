# Desenvolva um programa que leia o nome e duas notas de um aluno, calcule e mostrea a sua média.
# Esse programa é uma forma diferente de resolver o ecercício ex007

print('Inicio do programa!!!\n')

nome = str(input('Qual o nome do aluno: '))
N1 = float(input('\nDigite a primeira nota: '))
N2 = float(input('Digite a segunda nota: '))

print('\nA média do aluno {} foi de: {} '.format(nome, (N1 + N2)/2))

print('\nFim do programa!!!')
