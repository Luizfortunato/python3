"""Escreva um programa que pergunte a quantidade de KMs percorridos por um carro alugado e a quantidade de dias
 pelos quais ele foi alugado. 
 Coloque o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado."""

print(' *** Inicio do programa ***\n')

dias = int(input('Quantos dias o cliente permaneceu com o carro? '))
kms = float(input('Qual a quilometragem total percorrida nesses {} dias: '.format(dias)))

print('\nO valor total das despesas ficou em R${:.2f}'.format((dias*60.00) + (kms*0.15)))

print('\n*** Fim do programa ***')
