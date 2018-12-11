#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

grausC = float(input('Digite a temperatura em graus Celsius: '))
fare = ((9*grausC)/5)+32
print('A Temperatura de {}ºC convertida para farenheits fica {}ºF'.format(grausC, fare))