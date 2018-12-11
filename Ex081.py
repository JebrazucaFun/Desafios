'''
Exercício Python 081:
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

Lista = []

while True:
    Lista.append(int(input('Digite um número: ')))
    opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while opcao not in 'SN':
        opcao = str(input('Opção inválida! Deseja continuar? [S/N] ')).upper().strip()
    if opcao == 'N':
        break
print('*'*30)
print(f'Foram digitados {len(Lista)} valores.')
print(f'Valores digitados {sorted(Lista, reverse=True)}')
if 5 in Lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não foi localizado na lista.')
