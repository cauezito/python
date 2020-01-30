'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o
'''
soma = 0
for i in range(1, 7):
    print('Digite o número #{}:'.format(i))
    numero = int(input())
    if numero % 2 == 0:
        soma += numero
print('O resultado é: ' , soma)
