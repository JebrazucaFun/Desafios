'''
Exercício Python 073:
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
'''

ex = 'Tabela Brasileirão'
print('*-*'*15)
print(f'{ex:-^45}')
print('*-*'*15)
TabBrasileiro = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Atlético-PR',
                 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Corinthians', 'Ceará', 'Fluminense', 'Vasco',
                 'Chapecoense', 'América-MG', 'Sport', 'Vitória', 'Paraná')
print('')
print(f'Tabela Completa: {TabBrasileiro}')
print('')
print(f'Os primeiros Times da Tabela: {TabBrasileiro[0:5]}')
print(f'Os Últimos Times da Tabela: {TabBrasileiro[-4:]}')
print(f'Tabela em Ordem Alfaética: {sorted(TabBrasileiro)}')
print(f'O Chapecoense esta na {TabBrasileiro.index("Chapecoense")+1}º posição.')
