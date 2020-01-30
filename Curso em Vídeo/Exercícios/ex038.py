'''
Escreva um programa que leia DOIS NÚMEROS INTEIROS e compare-os, mostrando na tela a seguinte mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

numA = int(input('Número 1:'))
numB = int(input('Número 2:'))

if numA > numB:
    print('O primeiro valor é maior!')
elif numB > numA:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')