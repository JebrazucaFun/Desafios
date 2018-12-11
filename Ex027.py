'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
'''

nome = str(input('Digite seu nome completo: ')).strip()
nome_dividido = nome.split()
print(nome_dividido)
print('Prazer em te conhecer, {}'.format(nome))
print('Seu primeiro nome {} \n Seu ultimo nome {}.'.format(nome_dividido[0], nome_dividido[len(nome_dividido)-1]))


