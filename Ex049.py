'''
Relaça o DESAFIO 9, mostrado a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
'''

print(30*'\033[34m*\033[m')
print('{:^30}'.format('TABUADA'))
print(30*'\033[34m*\033[m')

num = int(input('Digite o número para saber a tabuada: '))
print((20*'\033[33m*\033[m'))
for c in range(0, 11):
    print('{} X {:2} = {}'.format(num, c, num*c))
print((20*'\033[33m*\033[m'))
print('{:^15}'.format('FIM'))

