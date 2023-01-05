""" Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50
por KM para viagens até 200Km e R$0,45 para viagens mais longas"""

distancia = float(input('\033[1;31mInforme a distância da sua viagem: '))

if distancia <= 200:
    valor = distancia * 0.50
    print('\033[1;33mO valor da sua viagem de {} Kms ficou em R${:.2f}'.format(distancia, valor))

else:
    valor = distancia * 0.45
    print('\033[1;34mO valor da sua viagem de {} Kms ficou em R${:.2f}'.format(distancia, valor))
