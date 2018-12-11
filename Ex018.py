'''
Programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

import math

print(13*'\033[32m-=-\033[m')
print('         VERIFICAÇÃO DO ANGULO')
print(13*'\033[32m-=-\033[m')

angulo = float(input('Digite o ângulo que vocẽ deseja os valores: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ãngulo de {}º tem o SENO de {:.2f}.'.format(angulo, seno))
print('O ângulo de {}º tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {}º tem a TANGENTE de {:.2f}'.format(angulo, tangente))
