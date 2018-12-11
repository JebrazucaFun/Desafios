'''
Faça um programa que leia um NUMERO INTEIRO e diga se ele é ou não um NUMERO PRIMO.
'''

num = int(input('Diga um numero: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[36m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\n\033[mO número {} foi divisivel {} vezes.'.format(num, total))
if total == 2:
    print('Desta forma, o número {} é \033[1mPRIMO.'.format(num))
else:
    print('Desta forma, o número {} \033[1mNÃO é PRIMO'.format(num))