""" Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles."""

from time import sleep
print('Contagem regressiva para os FOGOS!!!')

for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('\033[31mKKKKAAA\033[32mAAA\033[33mAABBBU\033[34mUUUM\033[35mMMM\033[36mMM!!!')
