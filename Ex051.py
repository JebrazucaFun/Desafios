'''
Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de um PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''

print(30*'\033[34m*\033[m')
print('{:^30}'.format('- 10 Termos de uma Progressão Aritimetica -'))
print(30*'\033[34m*\033[m')
termo1 = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
decimo = termo1 + (10) * razao
print('')
for c in range(termo1, decimo, razao):
    print('{}'.format(c), end=' → ')
print('FIM')