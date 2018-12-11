'''
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

print('*'*50)
print(f'{"LISTA DE PREÇOS":^50}')
print('*'*50)

Produtos = ('Monitor', 370, 'Teclado', 110, 'Mouse', 75.90,
            'Headset', 95.50, 'Carregador', 35, 'Modem', 145.70)

for pos, P in enumerate(Produtos):
    if pos % 2 == 0:
        print(f'{P:.<40}', end='')
    else:
        print(f'R$ {P:>.2f}')

print('*'*50)
