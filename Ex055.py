'''
Faça um programa que leia o PESO de CINCO PESSOAS.
No final, mostre qual foi o MAIOR e o MENOR peso lidos.
'''

peso_maior = 0
peso_menor = 0
for c in range(1, 6):
    peso = float(input('Diga o peso da {}º Pessoa: '.format(c)))
    if c == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso
print('O maior peso digitado foi {}Kg.\nO Menor peso digitado foi {}Kg'.format(peso_maior, peso_menor))
