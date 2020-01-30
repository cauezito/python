#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²
largura=(float(input('Digite a largura da parede: ')))
altura =(float(input('Digite a altura da parede: ')))
area = largura*altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m'.format(largura,altura,area))
tinta = area/2
print('Você precisará de {}l de tinta.'.format(tinta))