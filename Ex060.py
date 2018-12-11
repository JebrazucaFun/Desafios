'''
Faça um programa que leia um numero qualquer e mostre o seu fatorial.
Ex. 5! = 5x4x3x2x1= 120
Uma das respostas:

from math import factorial
n = int(input('Diga o número que queria saber o FATORIAL: '))
f = factorial(n)
print('O Fatorial de {} è {}.'.format(n, f)
'''

print(30*'\033[34m*\033[m')
print('{:^30}'.format('- Fatorial -'))
print(30*'\033[34m*\033[m')
fat = int(input('Diga o número que queria saber o FATORIAL: '))
cont = fat
resultado = 1
print('Calculando {}! = '.format(fat), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    resultado *= cont
    cont -= 1
print('{}'.format(resultado))
