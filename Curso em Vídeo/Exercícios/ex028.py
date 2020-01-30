'''
Escreva um programa que gere um número aleatório entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número gerado.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randrange
numero = int(randrange(0,5))
tentativa = int(input('Hit the number! [0 - 5]'))
if tentativa == numero:
    print('Congratulations! You re right!')
else:
    print('Nooop!')