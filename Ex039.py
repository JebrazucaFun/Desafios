'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date

print(40*'\033[35m*\033[m')
print('    Alistamento Militar       ')
print(40*'\033[35m*\033[m')
nascimento = int(input('Qual seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nascimento

print(' ')
print('Quem nasceu em {} esta com {} anos em {}.'.format(nascimento, idade, anoatual))
if idade == 18:
    print('Esta na hora de se alistar ao serviço militar.')
elif idade < 18:
    print('Ainda não esta na hora de se alistar ao serviço militar.')
    print('Falta {} anos para se alistar.'.format(18 - idade))
    ano = anoatual + (18 - idade)
    print('Seu alistamento será em {}.'.format(ano))
else:
    print('Já passou da hora de se alistar ao serviço militar.')
    print('Está com {} anos que passou do prazo.'.format(idade - 18))
    ano = anoatual + (18 - idade)
    print('Seu alistamento foi em {}.'.format(ano))

