""" Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:
— a vista dinheiro / cheque: 10% de desconto
— a vista no cartão: 5% de desconto
— em até 2X no cartão: preço formal
— 3X ou mais no cartão: 20% de juros """

print('\033[34m{:-^40}'.format(' LOJAS FORTUNATO '))  # {:^40} centraliza o texto ocupando um total de 80 caracteres

valor = eval(input('Informe o valor total das compras: R$ '))

print("""\033[33m\nFORMAS DE PAGAMENTO:
\033[33m[ 1 ] \033[34mà vista dinheiro / PIX
\033[33m[ 2 ] \033[34mà vista CARTÃO
\033[33m[ 3 ] \033[34m2X no CARTÃO
\033[33m[ 4 ] \033[34m3X ou mais no CARTÃo """)

forma_pgto = int(input('\033[33m\nQual a opção de pagamento?  '))

if forma_pgto == 1:
    print('\033[35mO total de suas compras foi R$ {:.2f} e com o desconto de 10% fica em R$ {:.2f}'
          .format(valor, valor - (valor * 0.1)))

elif forma_pgto == 2:
    print('\033[35mO total de suas compras foi de R$ {:.2f} e com o desconto de 5% fica em R$ {:.2f}'
          .format(valor, valor - (valor * 0.05)))

elif forma_pgto == 3:
    print('\033[35mO total de suas compras foi de R$ {:.2f}'.format(valor))
    print('\033[35mSerá parcelada em 2X sem juros de R$ {:.2f}'.format(valor / 2))

elif forma_pgto == 4:
    parcelas = int(input('\033[34mEm quantas vezes deseja parcelar? '))

    if parcelas == 1:
        print('\033[1;31mNão existe parcelamento em 1X. Selecione a opção para pagto à vista!!!')

    elif parcelas == 2:
        print('\033[1;31mUse a função [ 3 ] do menu. Refaça a operação!!!')

    elif 3 <= parcelas <= 12:
        print('\033[35mSuas compras serão parceladas em {}X com juros de 20%'.format(parcelas))

        total = valor + (valor * 0.2)

        print('\033[35mO valor total de suas compras ficou em R$ {:.2f} dividio em {}X de R${:.2f}'
              .format(total, parcelas, total / parcelas))

    elif parcelas > 12:
        print('\033[1;31mParcelamento máximo em 12X. Refaça a operação!!!')
else:
    print('\033[1;31mOpção inválida refaça a operação!!!')
