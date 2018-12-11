'''
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

Palavras =('rock', 'internet', 'computador', 'hack', 'programar', 'dinheiro',
           'filhos', 'casa', 'carro', 'televisor', 'cozinha', 'felicidade')

for P in Palavras:
    print(f'\nNa palavra {P.upper()} nos temos as vogais ', end=' ')
    for letra in P:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
