'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
indo de 10 até 0, com pausa de 1 segundo etre eles.
'''

from time import sleep

print(30*'\033[34m*\033[m')
print('     Contagem Regressiva     ')
print(30*'\033[34m*\033[m')

for c in range(0, 10):
    print(c)
    sleep(1)
print('{:*^40}'.format(' \033[32mFELIZ ANO NOVO!!! \033[m'))