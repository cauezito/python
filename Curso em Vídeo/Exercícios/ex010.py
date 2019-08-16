#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$1.00 = 3.00
print('Hi!')
real = float(input('How many R$ do you have?'))
dolar = real/3.00
print('You can buy: U${}'.format(dolar))