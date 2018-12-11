'''
Crie um programa que leia a IDADE e o SEXO de VÁRIAS PESSOAS. A cada pessoa cadastrada,
o programa deverá perguntar se o USUÁRIO quer ou não continuar.NO final,mostre:
A - Quantas pessoas tem mais de 18 ANOS.
B - Quantos HOMENS foram cadastrados.
C - Quantas MULHERES tem menos de 20 ANOS.
'''
ex = 'Cadastro de Pessoas'
Maior18 = homens = mulher20 = 0
while True:
    print('\033[34m=-=\033[m'*10)
    print(f'{ex:^30}')
    print('\033[34m=-=\033[m'*10)
    idade = int(input('Digite a idade: '))
    sexo = opcao = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        Maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    print('\033[34m*\033[m' * 30)
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('')
print(f'Total de pessoas com mais de 18 anos: {Maior18}')
print(f'Ao Todo temos {homens} homens cadastrado.')
print(f'Temos {mulher20} mulheres com menos de 20 anos.')