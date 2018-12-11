'''
Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 PESSOAS.
No final do programa,mostre:
- A média de idade do grupo.
- Qual é o nome do homem MAIS VELHO.
- Quantas mulheres tem menos de 20 anos.
'''

midade = 0
oldman = 0
oldname = str('')
agemulher = 0
for p in range(1, 5):
    print('{:-^30}'.format(' {}º PESSOA '.format(p)))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    midade += idade
    if sexo == 'M':
        if idade > oldman:
            oldman = idade
            oldname = nome
    else:
        if idade <= 20:
            agemulher += 1
print('')
print('A média de idade do grupo é de {}.'.format(midade/4))
print('O homen mais velho tem {} anos e se chama {}'.format(oldman, oldname))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(agemulher))
