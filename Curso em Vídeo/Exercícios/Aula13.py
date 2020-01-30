for i in range(0,7,2): #0 até 6 pulando de 2 em 2
    print(i)
print('FIM')

print('-'*40)
for c in range(10, 0, -1): #10 até 0
    print(c)
print('FIM')
print('-'*40)
x = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Passo:'))

for c in range(x, f+1, p):
    print(c)
print('FIM')
