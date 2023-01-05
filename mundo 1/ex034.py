""" Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$1250,00 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15% """

salario = eval(input('\033[1;31mQual o valor do salário do funcionário: R$ '))

if salario <= 1250.00:
    salario = salario + (salario * 0.15)

else:
    salario = salario + (salario * 0.10)

print('\033[1;35mO valor do seu novo salário já com o aumento é de \033[1;34mR$ {:.2f}'.format(salario))
