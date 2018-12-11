'''
Crie um programa que leia o NOME e o PREÇO de VÁRIOS PRODUTOS. O programa devera perguntar se o USUÁRIO vai continuar.
no Final mostre:
A - Qual é o total gasto na compra.
B - Quantos produtos custam MAIS de R$1000.
C - Qual é o NOME do produto MAIS BARATO.
'''

ex = 'LOJA JAM FAMILY'
print('\033[34m=-=\033[m'*10)
print(f'{ex:^30}')
print('\033[34m=-=\033[m'*10)
total = tot1000 = 0
cont = precmenor = 0
prodbarato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Valor: R$ '))
    total += preco
    if preco >= 1000: #Soma de produto para maiores de 1000
        tot1000 += 1
    if cont == 0 or procenor > preco: #verificação lógica de produto mais barato
        procenor = preco
        prodbarato = produto
    cont += 1
    print('\033[34m*\033[m'*30)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print('')
    if opcao == 'N':
        break
print(f'Foram {cont} itens com o Total da compra realizada foi R${total:.2f}')
print(f'Sendo {tot1000} produtos custando mais de R$1000.')
print(f'O produto escolhido mais barato foi {prodbarato} que custou R${procenor:.2f}.')