
from datetime import date
ano_nascimento = int(input('Qual o ano do seu nascimento? '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade < 18:
    print('Você ainda é muito novo para se alistar.')
    print('Ainda faltam {} anos ou {} meses para o seu alistamento'.format((18 - idade), (18 - idade) * 12))
    print('Seu alistamento será no ano {}'.format(ano_atual + (18 - idade)))

elif idade == 18:
    print('Você está com {} anos a idade correta de se alistar.'.format(idade))
    print('Procure a junta militar de sua cidade.')

else:
    print('Você está com {} nos e já deveria ter se alistado!!!'.format(idade))
    print('Está atrasado {} anos ou {} meses.'.format(idade - 18, (idade - 18) * 12))
    print('Seu alistamento foi no ano {}.'.format(ano_atual - (idade - 18)))
