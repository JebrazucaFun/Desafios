'''
Algoritmo que leia um numero
mostre o seu dobro, triplo e raiz quadrada.
raiz = n**(1/2)
'''

n1 = int( input('Digite um número: '))
dob = n1 * 2
tri = n1 * 3
raiz = n1**(1/2)
print('O dobro {} vale {}. \nO triplo de {} vale {}. \nA raiz quadrada de {} Vale {:.3f}.'.format(n1,dob,n1,tri,n1,raiz))