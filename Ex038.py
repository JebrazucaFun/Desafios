'''
Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

from time import sleep

print(40*'\033[35m*\033[m')
print('    Identificação do numero Maior       ')
print(40*'\033[35m*\033[m')

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

print('COMPARANDO...')
sleep(0.5)
if n1 == n2:
    print('OS dois números são IGUAIS!')
elif n1 > n2:
    print('O primeiro valor é o MAIOR!')
elif n2 > n1:
    print('O Segundo valor é o MAIOR')