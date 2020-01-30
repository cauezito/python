'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Tentar usar o ano do sistema
Seu programa também deverá mostrar o tempo que faltou ou passou do prazo.
'''
from datetime import datetime
anoNasc = int(input('Digite o ano de nascimento:'))
anoAtual = datetime.now().year
idade = int(anoAtual - anoNasc)
if anoAtual - anoNasc < 18:
   restante = 18 - idade
   print('Você se alistará em {} anos!'.format(restante))
elif idade == 18:
    print('Está na hora de você se alistar!')
elif idade >18:
    restante = idade - 18
    print('Já se passaram {} anos do prazo para se alistar'.format(restante))