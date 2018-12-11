'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas aqueles que forem pares.
Se o valor digitado for IMPAR, desconsiddere-o
'''

print(30*'\033[34m*\033[m')
print('{:^30}'.format('Soma dos Valores PARES'))
print(30*'\033[34m*\033[m')

soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite {}º número: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma dos {} valores PARES é {}.'.format(cont, soma))
print('FIM')