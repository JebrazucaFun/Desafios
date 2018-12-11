
'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o MAIOR e o MENOR valor lido.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

print(35*'\033[31m*\033[m')
print('\033[34m{:^35}\033[m'.format('Verificação dos Valores'))
print(35*'\033[31m*\033[m')
conf = 'S'
n = soma = maior = menor = contador = 0
while conf == 'S':
    n = int(input('Digite um número: '))
    conf = input('Deseja continuar? [S/N] ').upper()
    contador += 1
    soma += n
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Vocẽ digitou {} números e a média dos valores é {:.2f}.'.format(contador, soma/contador))
print('Sendo que o MAIOR valor foi {} e o MENOR foi {}.'.format(maior, menor))
print('FIM')