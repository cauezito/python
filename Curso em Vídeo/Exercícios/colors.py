#\033[STYLE; TEXT; BACKGROUND m opcionais e na ordem que quiser
'''
Style: 0 - nada 1 - negrito 4- underline 7 - negativo (inverte)
Text: 30 - Branco 31 - Vermelho 32 - Verde 33- Amarelo 34 - Azul 35 - Roxo 36 - Ciano 37- Cinza
Background 40 a 47 (na mesma ordem que o text)
'''

print('\033[0;30;41mOlá, Mundo!')
print('\033[4:33:44mOlá, Mundo!')
print('\033[1:35:43mOlá, Mundo!')
print('\033[30:42mOlá, Mundo!')
print('\033[mOlá, Mundo!')
print('\033[7;30mOlá, Mundo!')
print('\033[0;30;35mOi!')
nome = 'Luck'
print('Bem vindo, {}{}{}'.format('\033[2;34m', nome ,'\033[m'))
