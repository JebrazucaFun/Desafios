'''
Faça um programa que leia o SEXO de uma pessoa, mas s´o aceite os valores 'M' e 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

print(30*'\033[34m*\033[m')
print('{:^30}'.format('Verificação do Sexo'))
print(30*'\033[34m*\033[m')

dado = ' '
sex = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sex not in 'MF':
    print('Dado informado incorreto! Favor informar dado Válido.')
    sex = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
if sex == 'M':
    dado = 'Masculino'
else:
    dado = 'Feminino'

print('Vocẽ informou que seu sexo é {}.'.format(dado))
print('FIM')