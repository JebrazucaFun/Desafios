'''
Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS.
No Final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import date
ano = date.today().year
maior_idade = 0
menor_idade = 0
for c in range(1, 8):
    nascimento = int(input('Digite o {}º ano de nascimento: '.format(c)))
    if (ano - nascimento) >= 21:
        maior_idade += 1
    else:
        menor_idade += 1

print('Totalizando, {} pessoas tem maior idade. \n{} pessoas tem menor idade.'.format(maior_idade, menor_idade))