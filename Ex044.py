'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:

- A vista dinheiro/ cheque: 10% de desconto
- A vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

print(30*'\033[34m*\033[m')
print('     Pagamento de Produto     ')
print(30*'\033[34m*\033[m')

valor = float(input('Insira o valor do produto: R$'))
mpagameto = int(input('''
[ 1 ] A Vista Dinheiro / Cheque
[ 2 ] A vista no Cartão
[ 3 ] Até 2x no cartão
[ 4 ] 3x ou mais no cartão 

Escolha a opção de pagamento: '''))
print(30*'\033[32m*\033[m')
if mpagameto == 1:
    total = valor - (valor * 10)/ 100
elif mpagameto == 2:
    total = valor - (valor * 5) / 100
elif mpagameto == 3:
    valorp = valor / 2
    total = valor
    print('Valor em 2x de R${:.2f} SEM JUROS.'.format(valorp))
elif mpagameto == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = valor + (valor * 20)/100
    valorp = total / parcelas
    print('Valor em {}x de R${:.2f} COM JUROS.'.format(parcelas, valorp))
else:
    print('OPÇÃO INVALIDA DE PAGAMENTO!!!')
    total = valor

print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, total))