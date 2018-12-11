'''
Crie um programa que simule o funcionamento de um CAIXA ELETRÔNICO.
No inicio, pergunte ao usuário qual será o VALOR A SER SACADO (número inteiro) e
o programa vai informar quantas cédulas de cada valor serão entregues.
OBS. Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

ex = 'Banco do Povão'
print('\033[34m=-=\033[m'*10)
print(f'{ex:^30}')
print('\033[34m=-=\033[m'*10)
valor = int(input('Qual o valor a ser sacado? R$ '))
cedula = 50
total = valor
totalced = 0

while True:
    if total >= cedula:
        total -= cedula
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if total == 0:
            break

