'''
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''

print(30*'\033[34m*\033[m')
print('{:^30}'.format('NÚMEROS PARES'))
print(30*'\033[34m*\033[m')

for c in range(0, 51, 2):
    print(c, end=' ')
print('FIM')