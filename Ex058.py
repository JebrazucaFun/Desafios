'''
Melhore o jogo do DESAFIO 28
onde o computador vai 'pensar' em um numero entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.
'''

from random import randint
from time import sleep

print(13*'\033[34m-..-\033[m')
print('-------------- \033[32mJogo da Adivinhação v2.0 \033[m-------------')
print(13*'\033[34m-..-\033[m')
print('Teste sua sorte, Pensei em um numero entre 0 a 10')
print(' ')
numuser = int(input('Diga qual o número que eu pensei: '))
numpc = randint(0, 10) #número sorteado pelo computador.
cont = 0
#print('Eu pensei no numero {}'.format(numpc))
sleep(1)
while numuser != numpc:
    if numuser < numpc:
        print('MAIS... Tente mais uma vez.')
    elif numuser > numpc:
        print('MENOS... Tente outra vez.')
    cont += 1
    numuser = int(input('Qual o próximo palpite? '))
if cont == 0:
    print('Acertou de Primeira, Parabéns!')
else:
    print('Acertou com {} tentativas. Parabéns!'.format(cont))

print(6*'-'+'FIM'+6*'-')
