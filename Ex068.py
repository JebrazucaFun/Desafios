'''
Faça um programa que jogue PAR OU IMPAR com o computador. O Jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint
ex = 'Jogo do PAR ou IMPAR'
print('\033[34m=-=\033[m'*10)
print(f'{ex:^30}')
print('\033[34m=-=\033[m'*10)
ContaVitoria = 0
while True:
    jogador = int(input('Diga um valor: '))
    pc = randint(0, 10)
    jogadorpi = ' '
    while jogadorpi not in 'PI':
        jogadorpi = str(input('Par ou Ìmpar? [P/I] ')).strip().upper()[0]
    print('\033[32m-\033[m' * 30)
    total = jogador + pc
    print(f'Vocẽ jogou {jogador} e o computador {pc}. Total de {total}.', end=' ')
    print('DEU PAR!' if total % 2 == 0 else 'DEU IMPAR!')

    if jogadorpi == 'P':
        if total % 2 == 0:
            print('Parabéns, você venceu!')
            ContaVitoria += 1
        else:
            print('Que pena, você perdeu!')
            break
    elif jogadorpi == 'I':
        if total % 2 == 0:
            print('Parabéns, você venceu!')
            ContaVitoria += 1
        else:
            print('Que pena, você perdeu!')
            break
    print('Vamos jogar novamente...')
    '''
    bloco de comando realizado antes de correção
    if total % 2 == 0:
        pareimpar = 'P'
        print('Deu PAR')
    else:
        pareimpar = 'I'
        print('Deu ÌMPAR')
    if jogadorpi == pareimpar:
        print('Parabéns, Vocé Ganhou!')
    else:
        print('Que pena perdeu, mais sorte na próxima!')
        break
    ContaVitoria += 1
    '''

    print('\033[32m=\033[m' * 30)
print('\033[32m=\033[m' * 30)
print(f'GAME OVER! Você venceu {ContaVitoria} vezes.')