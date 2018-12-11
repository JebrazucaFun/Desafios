'''
Faça um programa que calcule a soma entre todos os números impares que são multiplos de três
e que se encontram no intervalo de 1 ate 500
'''

print(30*'\033[34m*\033[m')
print('{:^30}'.format('SOMA de Números IMPARES'))
print(30*'\033[34m*\033[m')

print('Números entre 1 até 500.')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma dos {} números neste intervalo é {}.'.format(cont, soma))