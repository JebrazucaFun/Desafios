'''
Crie um programa que leia vários inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a CONDIÇÂO DE PARADA.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag)
'''

cont = soma = 0
while True:
    n = int(input('Digite um número (999 para sair): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram digitados {cont} números. Sendo que o total da soma entre eles é {soma}')
print('FIM')
