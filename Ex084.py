'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

pessoas =list()
dados = []
pmaior = pmenor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()
    print('*'*30)
    while opcao not in 'SN':
        opcao = str(input('Opção Inválida. Deseja continuar? [S/N] ')).upper().strip()
    if opcao == 'N':
        break

#professor inseriu verificação do maior dentro do while
print(f'Foram cadastradas {len(pessoas)} pessoas.')
for cont, p in enumerate(pessoas):
    if cont == 0:
        pmaior = p[1]
        pmenor = p[1]
    if p[1] >= pmaior:
        pmaior = p[1]
    elif p[1] <= pmenor:
        pmenor = p[1]
print(f'O maior peso foi de {pmaior}Kg. ', end='')
for p in pessoas:
    if p[1] == pmaior:
        print(f'{p[0]}', end='')
print(f'\nO menor peso foi de {pmenor}Kg. ', end='')
for p in pessoas:
    if p[1] == pmenor:
        print(f'{p[0]}', end='')

