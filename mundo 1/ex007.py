# Desenvolva um programa que leia o nome e duas notas de um aluno, calcule e mostrea a sua média.

print('Inicio do programa!!!\n')

nome = str(input('Qual o nome do aluno: '))
N1 = float(input('\nDigite a primeira nota: '))
N2 = float(input('Digite a segunda nota: '))
media = (N1 + N2)/2

print('\nA média do aluno {} foi de: {:.1f} '.format(nome, media))

print('\nFim do programa!!!')

