'''
A Confederação Nacional de Nataçao precisa de um programa que leia o ano de nascimento de um atleta e
mostre sua categoria de acordo com a idade:

- Até 9 anos:MIRIM
- Até 14 anos:INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SENIOR
- Acima: MASTER
'''

from datetime import date

print(40*'\033[34m*\033[m')
print('   Confederação Nacional de Natação    ')
print(40*'\033[34m*\033[m')


nascimento = int(input('Diga o ANO de nascimento do atleta: '))
anoatual = date.today().year
idade = anoatual - nascimento

print('O atleta está com {} anos.'.format(idade))

if idade <= 9:
    print('Ele esta na categoria MIRIM.')
elif idade<= 14:
    print('Ele está na categoria INFANTIL.')
elif idade <= 19:
    print('Ele esta na categoria JUNIOR.')
elif idade <= 25:
    print('Ele está na categoria SENIOR.')
else:
    print('Ele esta na categoria MASTER.')
