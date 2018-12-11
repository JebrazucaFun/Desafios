'''
Escreva um programa que pergunte o salario de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais,o aumento é de 15%.
'''

print(30*'\033[4;32m*\033[m')
print('     Verificação Salário       ')
print(30*'\033[4;32m*\033[m')

sala = float(input('Digite o valor do seu salário:  R$ '))

if sala > 1250:
    saln = sala+((sala * 10)/100)
    proc = '10%'
else:
    saln = sala+((sala * 15)/100)
    proc = '15%'
print('Seu salário é R${:.2f}.'.format(sala))
print('Após aumento de {} Seu novo salário é R${:.2f}'.format(proc, saln))




