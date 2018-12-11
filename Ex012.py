'''
Programa que leia o preço de um produto e mostre sua novo preço,
com 5% de desconto.
'''

ProdP = float(input('Digite o preço do produto: R$ '))
Npreco = ProdP-(ProdP*5/100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(ProdP, Npreco))