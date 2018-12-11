'''
Exercício Python 080:
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
'''

Lista = list()

for val in range(0, 5):
    Num = int(input('Digite um valor: '))
    if val == 0 or Num > Lista[-1]:
        Lista.append(Num)
        print('Adicionado valor na ultima posição.')
    else:
        pos = 0
        while pos < len(Lista):
            if Num <= Lista[pos]:
                Lista.insert(pos, Num)
                print(f'Valor adicionado na {pos} posição.')
                break
            else:
                pos += 1
print('*'*30)
print(f'A lista em ordem é {Lista}')
