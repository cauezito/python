'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos
outros dois e maior que o valor absoluto da diferença entre essas medidas.
'''
print('Digite o comprimento de três retas:')
n1 = (float(input('Comprimento #1:')))
n2 = (float(input('Comprimento #2:')))
n3 = (float(input('Comprimento #3:')))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('As medidas podem formar um triângulo!')
else:
    print('As medidas não podem formar um triângulo!')

