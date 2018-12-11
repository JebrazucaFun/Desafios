'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa
Seu programa evera realiza a operaçãp solicitada em cada caso
'''

from time import sleep

print(30*'\033[34m*\033[m')
print('{:^30}'.format('Análise dos Valores'))
print(30*'\033[34m*\033[m')
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('informe o segundo valor: '))
opcao = soma = multi = 0
while opcao != 5:
    opcao = float(input('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    \nEscolha a opção que deseja realizar com os números digitados: '''))
    if opcao == 1:
        print(30 * '\033[34m*\033[m')
        soma = n1 + n2
        print('Os valores {} e {} somados são {}.'.format(n1, n2, soma))
    elif opcao == 2:
        print(30 * '\033[34m*\033[m')
        multi = n1 * n2
        print('Os valores {} e {} multipicados são {}.'.format(n1, n2, multi))
    elif opcao == 3:
        if n1 == n2:
            print(30 * '\033[34m*\033[m')
            print('Os valores são IGUAIS.')
        elif n1 > n2:
            print(30 * '\033[34m*\033[m')
            print('O valor {} é MAIOR que {}.'.format(n1, n2))
        else:
            print(30 * '\033[34m*\033[m')
            print('O valor {} é MAIOR que {}.'.format(n2, n1))
    elif opcao == 4:
        print(30 * '\033[34m*\033[m')
        print('Digite os novos valores.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao ==5:
        print('')
    else:
        print('')
        print('OPÇÂO INVÁLIDA, DIGITE NOVAMENTE.')
    sleep(1)
print('FIM')