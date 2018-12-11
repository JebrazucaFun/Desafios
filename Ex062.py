'''
Melhore o DESAFIO 061, perguntando para o usuáriose ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''

print(30*'\033[34m*\033[m')
print('{:^30}'.format('- Gerador de PA -'))
print(30*'\033[34m*\033[m')
termo1 = int(input('Diga o Primeiro Termo da PA: '))
razao = int(input('Diga a razão da PAss: '))
cont = total = 0
pa = termo1
mais = 10
while mais != 0:
    total += mais
    while cont < total:
        print(pa, end=' → ')
        pa += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Mais quantos termos quer mostrar? '))
print('Progressão realizada com {} termos mostrados.'.format(total))
