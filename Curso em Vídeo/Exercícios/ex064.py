'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
'''
parada = 0
quantidade = 0
while parada != 999:
    parada = int(input('Digite um número: '))
    quantidade += 1
    if parada == 999:
        print('Saindo...')
print('Média dos valores: ' , (parada) / (quantidade))
print('Foram digitados {} números!'.format(quantidade-1))
