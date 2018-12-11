'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.

'''

print(13*'-..-')
print('-------------- Radar Eletrônico -------------')
print(13*'-..-')
print(" ")
vel = float(input('Qual a velocidade do carro: '))

if vel > 80:
    print('Você foi multado, esta acima da velocidade limite de 80km/h.')
    multa = (vel - 80) * 7
    print('Você passou a {} km/h - Sua multa é de R${:.2f}'.format(vel, multa))
else:
    print('Vocẽ é um bom motorista e esta dentro da velocidade limite de 80km/h')
    print('Veloidade atual de {} km/h. \n Continue Assim!'.format(vel))
print('Tenha um bom dia. Dirija com segurança1')
print('-----FIM-----')