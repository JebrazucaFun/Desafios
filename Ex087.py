'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''


Matriz = [[], [], []]
soma = 0

# Inserindo valores na Matriz
for cont in range(0, 3):
    for c in range(0, 3):
        Matriz[cont].append(int(input(f'Digite um valor posição {cont} - {c}: ')))

# Verificação dos numeros pares
for pos, conta in enumerate(Matriz):
    for contt in Matriz[pos]:
        if contt % 2 == 0:
            soma += contt  # Incluindo a soma dos valores pares


som3cool = Matriz[0][2] + Matriz[1][2] + Matriz[2][2] # Soma 3º Coluna
linha2max = max(Matriz[1])
print()
print('*'*40)
print('Valores da Matriz 3x3 Digitada')
print(f'[ {Matriz[0][0]:^4} ] [ {Matriz[0][1]:^4} ] [ {Matriz[0][2]:^4} ]')
print(f'[ {Matriz[1][0]:^4} ] [ {Matriz[1][1]:^4} ] [ {Matriz[1][2]:^4} ]')
print(f'[ {Matriz[2][0]:^4} ] [ {Matriz[2][1]:^4} ] [ {Matriz[2][2]:^4} ]')
print('*'*40)
print(f'Soma dos valores pares digitados: {soma}')
print(f'Soma dos valores da terceira coluna: {som3cool}')
print(f'Maior valor da segunda linha: {linha2max}')