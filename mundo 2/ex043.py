""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu índice de massa corporal (IMC) e mostre
seu status conforme a tabela abaixo:
IMC abaixo de 18,5: Abaixo do peso
Entre 18,5 e 25: Peso ideal
Entre 25 e 30: Sobrepeso
Entre 30 e 40
Acima de 40: Obesidade mórbida """

peso = eval(input('Qual o seu peso (kg)? '))
altura = eval(input('Qual a sua altura (Mt)? '))
imc = peso / (pow(altura, 2))

print('O IMC para uma pessoa com {:.1f}Kgs e {:.2f}Mts é de {:.1f}'.format(peso, altura, imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO, cuidado!!!')

elif imc <= 25:
    print('Você está no peso ideal, parabéns!!!')

elif imc <= 30:
    print('Alerta, Você está com SOBREPESO!!!')

elif imc <= 40:
    print('Você está em OBESIDADE, cuidado!!!')

elif imc > 40:
    print('Atenção, você está em OBESIDADE MÓRBIDA, muito cuidado!!!')
