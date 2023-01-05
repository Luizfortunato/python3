""" Uma outra forma de resolver o exercício ex008 e adicionando funcionalidades
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros
e milimetros. """

print('Inicio do programa!!!\n')

metros = float(input('Digite uma distância em metros: '))

print('{} metros é o mesmo que:'.format(metros))

print('{} milimetros.'.format(metros*1000))

print('{} centimetros.'.format(metros*100))

print('{} decimetros.'.format(metros*10))

print('{:.3f} decâmetros.'.format(metros*0.1))

print('{} hectômetros.'.format(metros*0.01))

print('{} kilometros.'.format(metros*0.001))

print('\nFim do programa!!!')
