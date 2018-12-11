'''
Programa que leia a largura e a altura de uma parede em metros,
calcule a sua area e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta,
pinta uma área de 2m².
area = altura*largura
'''
LargP = float(input('Largura da Parede: '))
AltP = float(input('Altura da Parede: '))
area = LargP*AltP
tinta = area/2
print('Sua parede tem a dimensão de {}m x {}m e sua área é de {}M².'.format(LargP, AltP, area))
print('Desta forma, você precisará de {} litros de Tinta.'.format(tinta))