'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer
'''
from random import randrange
numero = int(randrange(0,10))
tentativa = int(input('Escolha um número de 0 a 10:   ' ))
qtdPalpites = 0
sair = False
while sair == True:
    print('Você errou! O computador pensou no número ', numero)
    qtdPalpites += 1
print('Você acertou em {} tentativas'.format(qtdPalpites))
