""" Faça um programa que leia 3 números e mostre qual é o menor e o maior entre eles. Outra forma de se resolver."""

numero1 = eval(input('\033[1;36mInforme o primeiro número: '))
numero2 = eval(input('\033[1;35mInforme o segundo número: '))
numero3 = eval(input('\033[1;34mInforme o terceiro número: '))

numeros = [numero1, numero2, numero3]                       # atribui os valores digitados a uma lista

print('\033[1;32mO MENOR valor digitado '
      'foi \033[1;31m{}\033[1;32m e o MAIOR valor foi \033[1;31m{}.'.format(min(numeros), max(numeros)))
