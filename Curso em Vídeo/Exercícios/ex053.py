'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
'''

print('=' * 30)
print('DESCOBRINDO PALÍNDROMOS!')
print('=' * 30)
frase = str(input('Digite uma frase: '))
#converte todas as letras para minúsculas
frase = frase.lower()
#remove acentuação e espaços em branco
frase = frase.replace(" ", "")
frase = frase.replace(",", "")
frase = frase.replace(".", "")
frase = frase.replace("?", "")
frase = frase.replace("!", "")
frase = frase.replace("-", "")
invertido = (frase[::-1])
if frase == invertido:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
