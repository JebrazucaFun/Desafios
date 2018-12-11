'''Exercício Python 079:
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
Lista = []
opcao = ''
while True:
    Num = (int(input('Digite Um valor: ')))
    if Num not in Lista:
        Lista.append(Num)
        print('Valor adiocionado.')
    else:
        print('Valor duplicado! Não será adicionado.')
    while opcao != 'S' and opcao != 'N':
        opcao = input('Deseja cotinuar? [S/N] ').upper()
        if opcao == 'N':
            break
print(Lista)