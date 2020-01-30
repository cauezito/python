'''
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais.
- Isósceles: dois lados iguais.
- Escaleno: todos os lados diferentes.
'''
print('Digite o comprimento de três retas:')
n1 = (float(input('Comprimento #1:')))
n2 = (float(input('Comprimento #2:')))
n3 = (float(input('Comprimento #3:')))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('As medidas podem formar um triângulo!')
    if n1 == n2 == n3:
        print('Equilátero')
    elif n1 != n2 and n1 != n3 and n2 != n1 and n2 != n3 and n3 != n1 and n3 != n2:
        print('Escaleno')
    elif n1 == n2 or n1 == n3 or n2 == n1 or n2 == n3 or n3 == n1 or n3 == n2:
        print('Isósceles')
else:
    print('As medidas não podem formar um triângulo!')