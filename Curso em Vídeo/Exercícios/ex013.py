#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
print('Hi!')
salary = float(input('Enter a salary: '))
increase = float(salary+(salary*0.15))
print('New salary: {}'.format(increase))