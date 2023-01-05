""" Exercício 022 Curso em vídeo

Crie um programa que leia o nome completo de uma pessoa e mostre:
— O nome com todas as letras maiúsculas e minúsculas.
— Quantas letras ao sem considerar espaços
— Quantas letras tem o primeiro nome
"""
from time import sleep
print('\033[1;31m*** Início do programa ***\033[m')

nome = str(input('\033[1mInforme seu nome completo: ')).strip()
print('\033[1;31m\nAnalisando seu nome...\n')
sleep(2)

print('\033[1;33mO seu nome em letras maiúsculas é: {}\n'.format(nome.upper()))
print('\033[1;34mO seu nome em letras minúsculas é: {}\n'.format(nome.lower()))

dividido = nome.split()
nome = nome.replace(" ", "")

print('\033[1;35mO seu nome completo é composto por {} letras.\n'.format(len(nome)))
print('\033[1;36mO seu primeiro nome é {} e ele tem {} letras\n'.format(dividido[0], len(dividido[0])))

print('\033[1;31m *** Fim do programa ***')
