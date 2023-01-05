""" Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais.
ISÓSCELES: dois lados iguais, um diferente.
ESCALENO: todos os lados diferentes.
"""
r1 = eval(input('\033[1;31mInforme o comprimento da primeira reta: '))
r2 = eval(input('\033[1;33mInforme o comprimento da segunda reta: '))
r3 = eval(input('\033[1;34mInforme o comprimento da terceira reta: '))

if (r2 - r3) < r1 < (r2 + r3) and (r1 - r3) < r2 < (r1 + r3) and (r1 - r2) < r3 < (r1 + r2):
    print('\033[1;32mCom os comprimentos acima É POSSÍVEL formar um triângulo!!!')

    if r1 == r2 == r3:
        print('O triângulo formado será do tipo EQUILÁTERO.')

    elif r1 == r2 or r1 == r3 or r3 == r2:
        print('O triângulo formado será do tipo ISÓSCELES.')

    elif r1 != r2 != r3 != r1:
        print('O triângulo formado será do tipo ESCALENO.')

else:
    print('\033[1;35mNÃO É POSSÍVEL formar um triângulo com os valores informados!!!')
