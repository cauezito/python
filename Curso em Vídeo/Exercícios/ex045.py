'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
computador = randint(1,3)

print('-'*30)
print('Jokenpô')
print('-'*30)

print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

usuario = int(input())

#EMPATE:
if computador == 1 and usuario == 1 or computador == 2 and usuario == 2 or computador == 3 and usuario == 3:
    print('Ninguém ganhou!')

#USUÁRIO VENCE:
elif computador == 1 and usuario == 2: #PAPEL VENCE PEDRA
    print('Você venceu!')
elif computador == 3 and usuario == 1: #PEDRA VENCE TESOURA
    print('O usuario venceu!')
elif computador == 1 and usuario == 3: #TESOURA VENCE PAPEL
    print('O usuario venceu')

#COMPUTADOR VENCE:
elif computador == 2 and usuario == 1: #PAPEL VENCE PEDRA
    print('O computador venceu!')
elif computador == 1 and usuario == 3: #PEDRA VENCE TESOURA
    print('O computador venceu!')
elif computador == 3 and usuario == 1: #TESOURA VENCE PAPEL
    print('O computador venceu!')
