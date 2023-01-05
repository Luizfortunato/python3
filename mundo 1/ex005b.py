# Faça um program que leia um número inteiro e mostra na tela o seu sucessor e o seu antecessor
# ex005b igual ex005 porém resolvido de uma maneira diferente

print('Inicio do programa!!!\n')

N = int(input('Digite o número para saber o seu sucessor e o seu antecessor: '))

Sucessor = N + 1
Antecessor = N - 1

print('\nO número digitado foi: {} '.format(N))

print('\nO sucessor do número {} é: {} '.format(N, Sucessor))

print('\nO antecessor do número {} é: {}'.format(N, Antecessor))

print('\nFim do programa!!!')
