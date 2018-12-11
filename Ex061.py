'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura WHILE
'''

print(30*'\033[34m*\033[m')
print('{:^30}'.format('- Gerador de PA -'))
print(30*'\033[34m*\033[m')
termo1 = int(input('Diga o Primeiro Termo da PA: '))
razao = int(input('Diga a razão da PAss: '))
cont = 0
pa = termo1
while cont < 10:
    print(pa, end=' → ')
    pa += razao
    cont += 1
print('FIM')
