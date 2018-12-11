# Criar um programa que faça o computador jogar Jokenpo com vocês.

from random import randint
from time import sleep

print(30*'\033[34m*\033[m')
print('     Jokenpo       ')
print(30*'\033[34m*\033[m')

print('Vamos jogar Jokenpo?')
itens = ('Pedra', 'Papel', 'Tesoura')
user = int(input('0 - Pedra\n1 - Papel\n2 - Tesoura\nFaça sua escolha: ' ))
pc = randint(1, 3)
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!!!')
sleep(1)

print(30*'\033[34m*\033[m')
print('Você escolheu \033[33m{}\nComputador escolheu \033[33m{}'.format(itens[user], itens[pc]))
print(30*'\033[34m*\033[m')

if pc == 0: # Joga Pedra
    if user == 1:
        print('Jogador Venceu!')
    elif user == 2:
        print('Computador Venceu!')
    elif user == 0:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA')
elif pc == 1: #Joga Papel
    if user == 0:
        print('Computador Venceu!')
    elif user == 2:
        print('Jogador Venceu!')
    elif user== 1:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA')
elif pc == 2: #Joga Tesoura
    if user == 1:
        print('Computador Venceu!')
    elif user == 0:
        print('Jogador venceu!')
    elif user == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA')

