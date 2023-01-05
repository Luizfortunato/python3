""" Crie um programa que mostre na tela todos os números pares no intervalo entre 1 e 50."""
from time import sleep
print('Esses são todos os números pares no intervalo entre 1 e 50:')
for numeros in range(2, 51, 2):
    print(numeros, end=' ')                     # end=' ' faz com que o print seja feito sempre na mesma linha.
    sleep(0.5)
print('Fim!!!')
