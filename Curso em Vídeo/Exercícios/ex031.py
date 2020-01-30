'''
Desenvolva um programa que pergunte a distância de uma viagem em KM, calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
e R$0,45 para viagens mais longas.
'''
distancia = (float(input('Digite a distância da viagem (km): ')))
if distancia <= 200:
    print('Total a pagar: R$' , distancia*0.50)
else:
    print('Total a pagar: R$' , distancia*0.45)