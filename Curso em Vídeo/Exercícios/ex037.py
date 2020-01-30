''''
Escreva um programa que leia um número inteiro qualquer e paça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''

num = int(input('Digite um número inteiro qualquer: '))
print('Escolha a base de conversão: ')
print('-' * 40)
print('[1] binário')
print('[2] octal')
print('[3] hexadecimal')
resposta = int(input())

if resposta == 1:
    binario = bin(num)
    print('O número convertido é: ' , binario)
elif resposta == 2:
    octal = oct(num)
    print('O número convertido é: ' , octal)
elif resposta == 3:
    hexadecimal = hex(num)
    print('O número convertido é: ' , hexadecimal)
