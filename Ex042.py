'''
Refaça o DESAFIO035 dos triangulos, acrescentando o recurso de mostrar que tipo e Triangulo sera formado:

- Equilatero:todos os lados iguais
- Isosceles:dois lados iguais
- Escaleno: Todos os lados diferentes

'''

print(30*'*')
print('     Analisador de Triângulo       ')
print(30*'*')

l1 = float(input('Digite um número: '))
l2 = float(input('Digite outro número: '))
l3 = float(input('Digite outro número: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2: #regra para se formar um triangulo.
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    if l1 == l2 == l3:
        print('EQUILÁTERO!')
    elif  l1 != l2 != l3 != l1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!.')
print(5*'-'+'FIM'+'-'*5)
