""" Faça um programa que pergunte o sexo da pessoa, caso seja feminino exibir a mensagem que o alistamento não se
aplica. Caso masculino, leia o ano de nascimento e informe a sua idade, se ele ainda vai se alistar ao serviço
militar, se é o ano exato de se alistar ou se já passou do tempo de alistamento. Seu programa também
 deverá mostrar o tempo que falta ou que passou do prazo """

from datetime import date

print("""Informe o seu sexo:
[1] Masculino
[2] Feminino""")

sexo = int(input('Digite o número correspondente ao seu sexo: '))
print(' ')
if sexo == 1:
    ano_nascimento = int(input('Informe o ano que você nasceu: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if idade < 18:
        print('Você ainda tem {} anos e não pode se alistar.'.format(idade))
        print('Ainda faltam {} anos ou {} meses para o seu alistamento.'.format(18 - idade, (18 - idade) * 12))
        print('O seu alistamento será em {}.'.format(ano_atual + (18 - idade)))

    elif idade == 18:
        print('Você está com {} anos a idade correta para se alistar.'.format(idade))
        print('Procure a junta militar de sua cidade.')

    elif idade > 18:
        print('Você esta com {} anos e já deveria ter se alistado!!!'.format(idade))
        print('Está atrasado {} anos ou {} meses'.format(idade - 18, (idade - 18) * 12))
        print('O ano do seu alistamento foi em {}'.format(ano_atual - (idade - 18)))

elif sexo == 2:
    print('Mulheres não precisam se alistar no serviço militar.')

else:
    print('\033[1;31mValor inválido!!!')
