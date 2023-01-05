""" Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar os 80Km/h, mostre uma mensagem informando
que ele foi multado.
A multa deve custar R$ 7,00 para cada KM acima do limite"""

velocidade = float(input('\033[1;31mQual a velocidade do veículo? '))
print('')
if velocidade <= 80:
    if velocidade > 75:
        print('\033[1;33mAtenção!!! Você está a {} Km/h o limite da via é de 80Km/h'.format(velocidade))
        print('\033[1;32mTenha um bom dia e faça uma boa viagem!!!')
    else:
       print('\033[1;32mVocê está a {:.0f} Km/h. Tenha um bom dia e faça uma boa viagem!!!'.format(velocidade))

else:
    print('\033[1;31mMultado!!!')
    print('Você ultrapassou o limite de velocidade da via!!!')
    print('\033[1;36mO valor da sua multa é de \033[1;33mR${:.2f}'.format(((velocidade - 80)*7)))
    