n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma dos números digitados é: ' , s)
print (f'A soma de {n1} e {n2} é {s}')
print('A soma vale {} '.format(s))

#ver o tipo primitivo da variável.
#se não for declarado um tipo antes do input, o padrão será String
var = int(input('Digite algum número aleatorio:'))
print(type(var))

#checar o tipo da variavel

teste = input('digite algo: ')
print(teste.isalnum()) #TESTE é ALFANUMÉRICO? True or False?
print(teste.isdecimal()) #TESTE é DECIMAL?
print(teste.isalpha()) #TESTE é alpha(betico)?
print(teste.islower()) #TESTE está em letras maiúsculas?


