'''
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

Numeros = list()
par = []
impar = []

while True:
    Numeros.append(int(input('Digite um número: ')))
    opcao = input('Deseja continuar? [S/N] ').upper().strip()
    while opcao not in 'SN':
        opcao = input('Opção invalida! Deseja continuar? [S/N] ').upper().strip()
    if opcao == 'N':
        break

for pos, val in enumerate(Numeros):
    if val % 2 == 0:
        par.append(val)
    else:
        impar.append(val)

print('*'*40)
print(f'Valores digitados {sorted(Numeros)}\nValores Pares {sorted(par)}\nValores Impares {sorted(impar)}')

