"""Crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
desse ângulo."""

from math import sin, cos, tan, radians

print('*** Início do programa ***\n')

angulo = float(input('Informe o valor de um ângulo: '))

print('\nO valor do SENO de {} é: {:.3f} '.format(angulo, sin(radians(angulo))))
print('O valor do COSSENO de {} é: {:.3f}'.format(angulo, cos(radians(angulo))))
print('O valor da TANGENTE de {} é: {:.3f}'.format(angulo, tan(radians(angulo))))

print('\n*** Fim do programa ***')
