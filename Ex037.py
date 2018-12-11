'''
EScreva um programa que leia um numero interiro qualquer e peça para usuario escolher
qual será a base da conversão:
- 1 para binario
- 2 para octal
- 3 para hexadecimal

'''

print(40*'\033[35m*\033[m')
print('     Conversão de Base Númerica       ')
print(40*'\033[35m*\033[m')

n1 = int(input('Digite um número inteiro: '))
print(''' Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opcao = int(input('Qual sua opção: '))
print('')
if opcao == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(n1, bin(n1)[2:]))
elif opcao == 2:
    print('O número {} convertido para OCTAL é {}'.format(n1, oct(n1)[2:]))
elif opcao == 3:
    print('O número {} convertido para HEXADECIMAL é {}'.format(n1, hex(n1)[2:]))
else:
    print('Opção INVÁLIDA!')
