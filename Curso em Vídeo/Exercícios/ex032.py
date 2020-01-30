#Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
ano = (int(input('Digite o ano para verificar.\n0 Para o ano atual:')))
if (ano == 0):
    ano = date.today().year
if(ano / 1 % 10 == 0 and ano / 10 % 10 == 0): #Pega a unidade e a dezena para verificar se é um ano centenário (00). Sem isso, exibiria "ano bissexto" para 1900, o que não é o caso.
    if (ano%400 == 0):
        print('O ano {} é bissexto!'.format(ano))
    else:
        print('O ano {} não é bissexto!'.format(ano))
elif(ano % 4 == 0):
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))
