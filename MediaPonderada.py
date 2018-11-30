print(30*'\033[34m*\033[m')
print('{:^30}'.format('- Média Inteiro Ponderada -'))
print(30*'\033[34m*\033[m')
A = int(input()) #peso 4
B = int(input()) #peso 6
mediap = (A*4 + B*6)//(4+6)
print(mediap)
