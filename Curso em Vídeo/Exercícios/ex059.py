'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso
'''
opcao = 0
while opcao != 5:
    print('-' * 40)
    print('Selecione um item')
    print('-' * 40)
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    print('')
    opcao = int(input())
    if opcao == 1:
        numA = int(input('Digite o primeiro número: '))
        numB = int(input('Digite o segundo número:'))
        print('O resultado é ' , numA + numB)
    elif opcao == 2:
        numA = int(input('Digite o primeiro número: '))
        numB = int(input('Digite o segundo número: '))
        print('O resultado é ' , numA * numB)
    elif opcao == 3:
        numA = int(input('Digite o primeiro número: '))
        numB = int(input('Digite o segundo número: '))
        if numA > numB:
            print('{} é maior que {}'.format(numA, numB))
        else:
            print('{} é maior do que {}'.format(numB , numA))
    elif opcao == 4:
        numA = int(input('Digite o primeiro novo número: '))
        numB = int(input('Digite o segundo novo número: '))

