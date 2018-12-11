'''
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e
preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
'''

Matriz = [[], [], []]

for cont in range(0, 3):
    for c in range(0, 3):
        Matriz[cont].append(int(input(f'Digite um valor posição {cont} - {c}: ')))
print('*'*40)
print('Valores da Matriz 3x3 Digitada')
print(f'[ {Matriz[0][0]:^4} ] [ {Matriz[0][1]:^4} ] [ {Matriz[0][2]:^4} ]')
print(f'[ {Matriz[1][0]:^4} ] [ {Matriz[1][1]:^4} ] [ {Matriz[1][2]:^4} ]')
print(f'[ {Matriz[2][0]:^4} ] [ {Matriz[2][1]:^4} ] [ {Matriz[2][2]:^4} ]')

