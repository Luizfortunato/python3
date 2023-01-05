""" Crie um programa que leia o comprimento do cateto oposto e cateto adjacente de um triangulo, calcule e mostre
o comprimento da hipotenusa. """

print('*** Inicio do programa ***\n')

oposto = float(input('Informe o comprimento do CATETO OPOSTO: '))
adjacente = float(input('Informe o comprimento do CATETO ADJACENTE: '))

from math import hypot

hipotenusa = hypot(oposto, adjacente)

print('Nesse caso temos um triângulo retângulo com as seguintes medidas:')
print('CATETO OPOSTO {} \nCATETO ADJACENTE {} \nHIPOTENUSA {:.3f}'.format(oposto, adjacente, hipotenusa))
print('\n*** Fim do programa ***')

