""" Faça um programa que leia 3 números e mostre qual é o menor e o maior entre eles."""
numero1 = eval(input('\033[1;32mInforme o primeiro número: '))
numero2 = eval(input('\033[1;33mInforme o segundo número: '))
numero3 = eval(input('\033[1;34mInforme o terceiro valor: '))

menor = numero1

if numero2 < numero1 and numero2 < numero3:
    menor = numero2

if numero3 < numero1 and numero3 < numero2:
    menor = numero3

maior = numero3

if numero1 > numero3 and numero1 > numero2:
    maior = numero1

if numero2 > numero3 and numero2 > numero1:
    maior = numero2

print('\033[1;35mO MENOR número digitado foi {} e o MAIOR foi {}'.format(menor, maior))
