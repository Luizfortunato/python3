""" A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, conforme a idade
— Até 9 anos: Mirim
— Até 14 anos: INFANTIL
— Até 19 anos: JÚNIOR
— Até 25 anos: SÊNIOR
— Acima de 25 anos: MASTER """

from datetime import date

ano_nascimento = int(input('Em que ano o atleta nasceu? '))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')

elif 9 < idade <= 14:
    print('classificação: INFANTIL')

elif 14 < idade <= 19:
    print('Classificação: JÚNIOR')

elif 19 < idade <= 25:
    print('Classificação: SÊNIOR')

else:
    print('Classificação: MASTER')
    