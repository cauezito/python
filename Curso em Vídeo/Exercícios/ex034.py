'''
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
Para salários superiores a R$1.250,00 calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%
'''
salario = float(input('Digite o salário: '))
if(salario <= 1250):
    novoSalario = (salario * 15 / 100) + salario
    print('O novo salário é de: {:.2f}'.format(novoSalario))
else:
    novoSalario = (salario * 10 / 100) + salario
    print('O novo salário é de: {:.2f}'.format(novoSalario))