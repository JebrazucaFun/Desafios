'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

diasA = int(input('Quantos dias alugados? '))
km = float(input('Quantos Kilometros foram percorridos? '))
Totdia = diasA*60
Totkm = km*0.15
print('A Carro foi alugado por {} dias e percorrido {} km, Totalizando R${:.2f} a ser pago.'.format(diasA, km, Totdia+Totkm))