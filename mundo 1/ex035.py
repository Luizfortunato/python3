""" Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
triângulo."""

r1 = eval(input('\033[1;31mInforme o comprimento da primeira reta: '))
r2 = eval(input('\033[1;33mInforme o comprimento da segunda reta: '))
r3 = eval(input('\033[1;34mInforme o comprimento da terceira reta: '))

if (r2 - r3) < r1 < (r2 + r3) and (r1 - r3) < r2 < (r1 + r3) and (r1 - r2) < r3 < (r1 + r2):
    print('\033[1;32mCom os comprimentos acima É POSSÍVEL formar um triângulo!!!')

else:
    print('\033[1;35mNÃO É POSSÍVEL formar um triângulo com os valores informados!!!')
