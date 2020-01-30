'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa. Calcule e mostre seu IMC
de acordo com a tabela:

- Abaixo de 18.5: Abaixo do peso.
- Entre 18.5 e 25: Peso ideal.
- 25 até 30: Sobrepeso.
- 30 até 40: Obesidade.
- Acima de 40: Obesidade mórbida.
'''

peso = float(input('Digite o seu peso:'))
altura = float(input('Digite a sua altura:'))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal!')
elif imc >= 25 and imc <= 30:
    print('Você está em sobrepeso!')
elif imc >= 30 and imc <=40:
    print('Você está obeso!')
elif imc > 40:
    print('Obesidade mórbida!')