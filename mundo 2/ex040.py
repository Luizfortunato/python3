""" Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final conforme
a média atingida:
— Média abaixo de 5,0: REPROVADO
— Média entre 5,0 e 6,9: RECUPERAÇÃO
— Média 7.0 ou superior: APROVADO
"""

N1 = eval(input('Informe a primeira nota: '))
N2 = eval(input('Informe a segunda nota: '))
media = (N1 + N2) / 2

print('Com as notas {:.1f} e {:.1f} sua média final é {:.1f}!!!'.format(N1, N2, media))
if media < 5.0:
    print('\033[1;31mAluno REPROVADO!!!')

elif 5 <= media <= 6.9:
    print('\033[1;33mAluno em RECUPERAÇÃO!!!')

elif media >= 7.0:
    print('\033[1;32mAluno APROVADO!!!')
