'''
Desenvolva um programa que leia nome, idade e gênero de 4 pessoas. No final do programa , mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos.
'''
media = 0
homemMaisVelho = ""
maiorIdadeHomem = 0
mulherMenor20 = 0

for i in range(1,5):
    nome = str(input('Digite o seu nome:'))
    idade = int(input('Digite a sua idade: '))
    genero = str(input('Digite o seu gênero [f/m]: '))
    media+=idade
    if genero == 'm' :
        if idade > maiorIdadeHomem:
            homemMaisVelho = nome
    if genero == 'f':
        if idade < 20:
            mulherMenor20 += 1
print('*' * 35)
print('A média de idade do grupo é de: {}'.format(media/4))
if homemMaisVelho != "":
    print('O nome do homem mais velho é: ' , homemMaisVelho)
print('{} mulheres têm menos de 20 anos!'.format(mulherMenor20))