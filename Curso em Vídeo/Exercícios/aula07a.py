#criar a raíz quadrada de um número é a mesma coisa de calcular a sua potência por 1/2
num = float(81**(1/2))
print (num)

print('='*35)
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {:20}'.format(nome))
print('Digite dois números para a soma:')
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
print('A soma vale {}'.format(n1+n2), end='') #não quebrar a linha
m = n1 * n2
d = n1/n2
di = n1//n2
e = n1 ** n2
print('A multiplicação vale {} , a divisão vale {:.2f} \n a divisão inteira vale {} e a exponenciação vale {}'.format(m,d,di,e))
