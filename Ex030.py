'''
Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR
'''

print(30*'*')
print('     Número PAR ou IMPAR ?       ')
print(30*'*')
num = int(input('Me Diga um número: '))

if (num % 2) == 0:
    print('O Número {} é PAR!'.format(num))
else:
    print('O Número {} é IMPAR!'.format(num))
print('----FIM-----')