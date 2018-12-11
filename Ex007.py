'''
Programa que leia as duas notas de um aluno
calcule e mostre sua média
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a Segunda nota; '))

m = (n1 + n2) / 2
print('A Média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1,n2,m))