'''
Crie um prorama que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
Maioridade: 21 anos.
'''
from datetime import datetime
dataNasc = 0
dataAtual = datetime.now().year
soma = 0
for i in range(1,8):
    dataNasc = int(input('Digite o ano de nascimento:'))
    if dataAtual - dataNasc >= 21:
        soma+=1
        print('Você já atingiu a maioridade!')
        print('-'*30)
    else:
        print('Você ainda não atingiu a maioridade!')
        print('-'*30)
print('Da lista, {} pessoas já atingiram a maioridade' . format(soma))
