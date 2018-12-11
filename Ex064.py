'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999,que é a condição de parada. No final, mostre quantos numeros foram digitados
e qual foi a soma entre eles (desconsiderando o flag)
'''

print(35*'\033[31m*\033[m')
print('\033[34m{:^35}\033[m'.format('Soma dos Valores'))
print(35*'\033[31m*\033[m')
numero = contador = soma = 0
while numero != 999:
    numero = int(input('Digite um número: (Caso queira parar (999) '))
    if numero != 999:
        soma += numero
        contador += 1
print('Você digitou {} números e a soma entre eles é {}.'.format(contador, soma))
