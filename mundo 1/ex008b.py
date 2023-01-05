""" Uma outra forma de resolver o exercício ex008
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros
e milimetros. """

print('Inicio do programa!!!!\n')

M = float(input('Digite o valor em metros que deseja converter: '))

CM = M * 100
MM = M * 1000

print('\n{:.2f} metros equivalem a {:.2f} centimetros.'.format(M, CM))

print('\n{:.2f} metros equivalem a {:.2f} milimetros.'.format(M,MM))

print('\nFim do programa!!!')

