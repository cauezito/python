'''
Faça um programa que leia o gênero de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto
'''
gen = str(input('Digite o seu gênero: [F/M]: ')).strip().upper()[0]
while gen not in 'MmFf':
    gen = str(input('Dados inválidos, por favor digite o seu gênero: [F/M]: ')).strip().upper()[0]
print('Gênero registrado')