"""Escreva um programa que leia um valor em metros e o exiba convertido em centímetros
e milimetros."""

print('Inicio do programa!!!\n')

M = float(input('Digite o valor em metros: '))

print('\n{:.1f} metros equivalem a {:.0f} centimetros e {} milimetros.'.format(M, M*100, M*1000))

print('\nFim do programa!!!')
