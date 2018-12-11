'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"
'''

from time import sleep
cid = str(input('Digite sua cidade: ')).split()
sleep(3)
print('SANTO' == cid[:5].upper())

