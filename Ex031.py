'''
Desenvolva um programa que pergunte a distância de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200km
e R$0,45 para viagens mais longas.
'''


print(30*'*')
print('     Custo de Viagem       ')
print(30*'*')

dist = float(input('Diga qual será a distância da viagem em KM: '))
'''
if dist <= 200:
    valor = dist * 0.50
    print('A distância da viagem é {}KM e o valor da passagem será R${:.2f}'.format(dist, valor))
else:
    valor = dist * 0.45
    print('A distâcia da viagem é {}KM e o valor da passagem será R${:.2f}'.format(dist, valor))
'''
print('Sua viagem será de {}KM'.format(dist))
valor = dist * 0.50 if dist <= 200 else dist * 0.45 # outra forma de condição simplificada no Python
print('O preço da sua passagemserá de R${:.2f}'.format(valor))
print('Tenha uma Boa Viagem!')

