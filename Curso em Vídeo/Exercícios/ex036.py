'''
Escreva um programa para aprovar o emprésimo bancário para a compra de uma casa. O programa vai
perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ELE VAI PAGAR.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''

valorCasa = float(input('Qual é o valor da casa?'))
salario = float(input('Qual é o seu salário?'))
qtdMeses = int(input('Em quantos meses você pagará?'))
valorPrestacao = valorCasa / qtdMeses
if valorPrestacao > (30 * salario) / 100:
    print('Lamento! Empréstimo negado por exceder 30% do seu salário!')
else:
    print('Empréstimo aceito!')