'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:

-À vista dinheiro/cheque: 10% de desconto.
-À vista no cartão: 5% de desconto.
-Em até 2x no cartão: preço normal.
-3x ou mais no cartão: 20% de juros.
'''
valorProduto = float(input('Digite o valor do produto:'))
print('-' * 40)
print('Escolha a condição de pagamento:')
print('[1] À vista no dinheiro ou cheque (10% de desconto)')
print('[2] À vista no cartão (5% de desconto)')
print('[3] Em até 2x no cartão (preço normal)')
print('[4] 3x ou mais no cartão (20% de juros')
print('-' * 40)
condicao = int(input())

if condicao == 1:
    print('Você pagará {} no produto!'.format(valorProduto * 0.9))
elif condicao == 2:
    print('Você pagará {} no produto!'.format((valorProduto * 5 / 100)) + valorProduto)
elif condicao == 3:
    print('Você pagará {} no produto!'.format(valorProduto))
elif condicao == 4:
    print('Você pagará {} no produto!'.format(valorProduto * 1.20))
else:
    print('Opção inválida!')