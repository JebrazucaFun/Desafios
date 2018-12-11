'''Exercício Python 078:
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

ValoresN = []
for val in range(5):
    ValoresN.append(int(input('Digite um Valor: ')))
print('#'*30)
print(f'Você digitou os valores : {ValoresN}')
print(f'O maior valor digitado foi {max(ValoresN)} e esta nas posições: ', end='')
for pos, v in enumerate(ValoresN):
    if v == max(ValoresN):
        print(f'{pos}... ', end=' ')
print()
print(f'O menor valor digitado foi {min(ValoresN)} e esta nas posições: ', end='')
for pos, v in enumerate(ValoresN):
    if v == min(ValoresN):
        print(f'{pos}... ')
print()
