'''
Programa que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento.
'''
Sal = float(input('Digite o salário do funcionário: R$ '))
Nsal = Sal+(Sal*15/100)
print('O Salário de R$ {:.2f} teve um aumento de 15%, passa a receber R${:.2f}'.format(Sal, Nsal))