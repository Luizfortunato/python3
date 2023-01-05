""" Escreva um programa que leia dois números inteiros e compare-os mostrando uma mensagem na tela:
— O primeiro valor é maior
— O segundo valor é maior
— Não existe valor maior, os dois são iguais """

numero1 = eval(input('\033[36mInforme o primeiro valor a ser comparado: '))
numero2 = eval(input('\033[32mInforme o segundo valor a ser comparado: '))

if numero1 > numero2:
    print('\033[34mO primeiro valor é o maior')

elif numero2 > numero1:
    print('\033[35mO segundo valor é o maior')

else:
    print('\033[31mNão existe valor maior, os dois são iguais!!!')
