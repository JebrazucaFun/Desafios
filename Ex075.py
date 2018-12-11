'''
 Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
 No final, mostre:
 A) Quantas vezes apareceu o valor 9.
 B) Em que posição foi digitado o primeiro valor 3.
 C) Quais foram os números pares.
'''

Valores = (int(input('Digite um número: ')), int(input('Digite mais um número: ')),
           int(input('Digite outro número: ')), int(input('Digite o ultimo número: ')))
print(f'Você Digitou os valores: {Valores}')
print(f'O número 9 apareceu {Valores.count(9)} vezes')
if 3 in Valores:
    print(f'O número 3 Foi digitado na posição: {Valores.index(3)}')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
print(f'Os números pares digitados foram: ', end='')
for n in Valores:
    if n % 2 == 0:
        print(f'{n}', end=' ')



