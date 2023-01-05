""" Faça um programa que leia o nome completo de uma pessoa, mostrando em seguido o primeiro e o último nome
separadamente.
EXEMPLO: Ana Maria de Souza
Primeiro: Ama
Último: Souza
"""
from time import sleep
print('\033[1;031m*** Início do programa ***\n\033[m')

nome = str(input('\033[1;033mInforme seu nome completo: ')).strip()
print('\033[1;032mMuito prazer em te conhecer!!!')
print('\033[1;035mAnalisando seu nome...')
sleep(2)
nome = nome.split()
print('\033[1;036mSeu primeiro nome é: {}'.format(nome[0]))
print('\033[1;034mSeu último nome é: {}'.format(nome[-1]))

print('\n\033[1;031m*** Fim do programa ***')
