""" Faça um programa que mostre todos os múltiplos de 3 no intervalo entre 1 e 500. Após calcule a somatória entre
todos os valores ímpares """

print('Esse são todos os multiplos de 3 no intervalo entre 1 até 500:')
soma = 0
cont = 0
for numeros in range(3, 499, 3):
    print(numeros, end=' ')
    if numeros % 2 != 0:
        soma += numeros                                 # += equivale a 'soma = soma + numeros'
        cont += 1                                       # += equivale a 'cont = cont + 1

print('\n')
print('Entre esses valores existem {} números ímpares e a somatória de todos ele é {}'.format(cont, soma))
print('Fim!!!')
