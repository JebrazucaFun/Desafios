'''
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

Numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
         randint(1, 10), randint(1, 10))
print('Os Números sorteados foram: ', end=' ')
for num in Numeros:
    print(f'{num} ', end= ' ')
print(f'\nO Maior valor sorteado é {max(Numeros)}')
print(f'O Menor valor sorteado é {min(Numeros)}')