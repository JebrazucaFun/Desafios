'''
Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o numero escolhido pelo computador.
O programa devera escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep

print(13*'-..-')
print('-------------- Jogo da Adivinhação v1.0 -------------')
print(13*'-..-')
print('Teste sua sorte, Escolha em um numero entre 0 a 5')
print(' ')
numuser = int(input('Diga qual o número que eu pensei: '))
numpc = randint(0, 5) #número sorteado pelo computador.
#print('Eu pensei no numero {}'.format(numpc))
print('PENSANDO....')
sleep(2)
if numpc == numuser:
    print('Parabéns, acertou! Você ganhou! Digitou o mesmo número que pensei.')
    print('Número {}'.format(numuser))
else:
    print('Que pena, Eu ganhei!')
    print('Digitou o número {} e eu pensei no número {}'.format(numuser, numpc))
print(6*'-'+'FIM'+6*'-')
