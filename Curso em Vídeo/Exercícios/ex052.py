'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
divisíveis APENAS por um e por ele mesmo.


'''
numero = int(input('Digite um número inteiro:'))
if numero > 1 and numero % 2 != 0:
    if numero % numero == 0:
        print('{} é um número primo!'.format(numero))
else:
    print('{} não é um número primo!'.format(numero))