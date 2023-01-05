""" Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area
toral e a quantidade de tinta necessária para pinta-la.
 Sabendo que cada litro de tinta pinta uma área de 2M² """

print('Inicio do programa!!! \n')

altura = float(input('Digite qual a altura em metros da parede que deseja pintar: '))
largura = float(input('Digite qual a largura em metros da parede: '))
area = altura * largura

print('\n A sua parede tem a dimenssão de {:.2f} x {:.2f} e sua área é de {:.2f} M².'.format(altura, largura, area))

tinta = area/2

print('\nPara pintar os {} M2 de sua parede voce irá precisar de {} litros de tinta.'.format(area, tinta))

print('\nFim do programa!!!')
