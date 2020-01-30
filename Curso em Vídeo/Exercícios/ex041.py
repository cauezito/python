'''
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos : MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima:       MASTER
'''
from datetime import datetime

anoNasc = int(input('Digite o ano de nascimento:'))
anoAtual = datetime.now().year

if anoAtual - anoNasc <= 9:
    print('Mirim')
elif anoAtual - anoNasc <=14:
    print('Infantil')
elif anoAtual - anoNasc <=19:
    print('Junior')
elif anoAtual - anoNasc <=20:
    print('Sênior')
elif anoAtual - anoNasc >20:
    print('Master')
