'''
Faça um programa que mostre a TABUADA de VÁRIOS NÚMEROS, um de cada vez,
para cada valor digitado pelo usuário. O programa será INTERROMPIDO
quando o número soliitado for NEGATIVO.
'''
ex = 'Tabuada'
print('\033[32m=-=\033[m'*10)
print(f'{ex:^30}')
print('\033[32m=-=\033[m'*10)

while True:
    cont = 1
    n = int(input('Qual tabuada gostaria de ver? '))
    print('\033[36m***\033[m' * 10)
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} x {cont:2} = {n*cont}')
        cont += 1
    print('\033[36m***\033[m'*10)
print('Programa Encerrado Finalizado, Volte Sempre!')

