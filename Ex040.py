'''
Crie um programa que leia duas notas de um aluno e calcule sua media,
mostrando uma mensagem no final, de acordo com a media atingida

- Média abaixo de 5.0 REPROVADO
- Média entre 5.0 e 6.9 RECUPERAÇÂO
- Média 7.0 ou superior APROVADO
'''

print(30*'\033[34m*\033[m')
print('     Notas dos Alunos       ')
print(30*'\033[34m*\033[m')

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1+n2)/2

print(30*'\033[34m*\033[m')
print('Com as notas {} e {}.'.format(n1, n2))
if media >= 7:
    print('A Média do aluno é \033[1;36m{}!'.format(media))
    print('\033[mAluno \033[1;36mAPROVADO!\033[m')
elif 7 > media >= 5: #outro metodo para recuperação (if 7 > media >= 5:
    print('A Média do aluno é \033[35m{}!'.format(media))
    print('\033[mAluno em \033[35mRECUPERAÇÃO!\033[m')
else:
    print('A Média do aluno é \033[31m{}!'.format(media))
    print('\033[mAluno \033[31mREPROVADO!\033[m')