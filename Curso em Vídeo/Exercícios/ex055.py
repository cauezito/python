'''
Faça um programa que leia o peso de cinco pessoas, no final, mostre qual foi o maior e menor pesos lidos.
'''
maior = 0
menor = 100000

for i in range(1,6):
    peso = float(input('Digite o peso #{}:'.format(i)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso digitado foi: ' , maior)
print('O menor peso digitado foi: ' , menor)
