'''
Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:

- Abaixo de 18.5: abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 ate 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40:Obesidade Morbida

'''

print(30*'\033[35m*\033[m')
print('         CALCULO IMC    ')
print(30*'\033[35m*\033[m')

peso = float(input('Diga seu peso: '))
altura = float(input('Diga sua altura: '))
imc = peso / (altura*altura)
print(30*'\033[35m*\033[m')
print('Sua altura é {} com {} quilos'.format(altura, peso))
print('Seu IMC é {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está Abaixo do Peso!')
elif imc <= 25:
    print('Você está com o Peso ideal.')
elif imc <= 30:
    print('Você está com Sobrepeso!')
elif imc <= 40:
    print('Você está com Obesidade!')
else:
    print('Você está com \033[33mOBESIDADE MORBIDA!!!\033[m')
