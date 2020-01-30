'''
Crie um programa que leia vários numeros inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

continuar = 's'
maior = 0
menor = 10000000000
media = 0
soma = 0
while continuar == 's':
    for i in range(1,6):
        num = int(input('Digite um valor:'))
        soma += num
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    print("Maior valor lido: " , maior)
    print("Menor valor lido: " , menor)
    print("Soma de todos os valores: " , soma)
    continuar = input('Deseja continuar? [s/n]')