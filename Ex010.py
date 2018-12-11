'''
Programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar.
Condsidere - us$1,00 = R$3.27
'''

reais = float( input('Quanto de dinheiro tem na carteira? R$ '))
dolar = reais/3.27
euro = reais/4.20
bitcoin = reais/27.989,25
libra = reais / 4.869
print('Com R${:.2f} você poderá comprar:\nU$ {:.2f} Doláres.'.format(reais, dolar))
print('€ {:.2f} Euros'.format(euro))
print('$ {:.2f} Libras'.format(libra))
print('{} Bitcoins'.format(bitcoin))
