'''
Desenvolva um programa que leia tres retas e diga ao usuario se elas podem ou não formar um triangulo
'''

print(30*'*')
print('     Analisador de Triângulo       ')
print(30*'*')

l1 = float(input('Digite um número: '))
l2 = float(input('Digite outro número: '))
l3 = float(input('Digite outro número: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2: #regra para se formar um triangulo.
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!.')
print(5*'-'+'FIM'+'-'*5)
