'''
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez
e em que posição ela aparece a ultima vez
'''

frase = str(input('Diga uma frase: ')).lower().strip()
print('A letra A aparece {} vezes em sua frase'.format(frase.count('a')))
print('A primeira letra A aparece na posição {} '.format(frase.find('a')+1))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('a')+1))
