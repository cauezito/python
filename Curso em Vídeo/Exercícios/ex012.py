#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5%de desconto
price = float(input('Enter product price:'))
nPrice = price - (price*0.05)
print('New price:' , nPrice)