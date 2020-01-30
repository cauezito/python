'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que foi multado.
A multa custará R$7,00 por cada Km acima do limite.
'''
velocidade = (float(input('Digite a velocidade do carro: ')))
if velocidade>80.0:
    multa=7.00
    velocidade = velocidade-80
    print('Você foi multado!')
    print('Total a pagar: ', velocidade*multa)
else:
    print('Okay!')

