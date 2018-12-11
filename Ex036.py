'''
Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da casa
o Salário do comprador e em quantos anos ela vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo sera negado

'''

print(40*'\033[34m*\033[m')
print('     Verificação de Empréstimo       ')
print(40*'\033[34m*\033[m')

vc = float(input('Diga o valor da casa: R$'))
sc = float(input('Diga o seu sálario: R$'))
ap = int(input('Diga em quantos anos será pago: '))
precano = int(ap * 12) # inserindo quantos parcelas serão feitas.
prestacao = vc / precano # valor da prestação
print(40*'\033[34m*\033[m')
print('O valor da casa será R${:.2f} e seu salário é de R${:.2f}'.format(vc, sc))
print('Empréstimo sera R${:.2f} em {} Vezes.'.format(prestacao,precano))

if prestacao > (sc*30)/100: #verificação para ser aprovado emprestimo
    print('O Empréstimo será \033[1;31mNEGADO\033[m')
else:
    print('O Empréstimo será \033[1;32mAPROVADO\033[m')


