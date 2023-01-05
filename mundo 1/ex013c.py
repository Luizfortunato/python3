"""Elabore um programa que le o preço de um produto e informa o valor com o de desconto para pagamento a
vista e parcelado.

a vista == 15% de desconto
a prazo == 08% de desconto"""

print('*** Inicio do programa ***\n')

preco = float(input('Informe o valor do produto R$:'))

avista = preco - (preco * 15/100)
aprazo = preco - (preco * 8/100)

print('O produto que custava R${:.2f} fica R${:.2f} para pagamento a vista e R${:.2f} para '
      'pagar parcelado.'.format(preco, avista, aprazo))

print('\n*** Fim do programa ***')
