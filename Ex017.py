'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.

'''
from math import hypot

c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento do cateto adjaente:'))
# Metodo para calculo hipotenusa - hip = (c1 ** 2 + c2 ** 2) ** (1/2)
hip = hypot(c1, c2)
print('A Hipotenusa vai medir {:.2f}'.format(hip))
