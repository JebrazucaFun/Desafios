'''
Programa que leia um valor em metros
e o exiba convertido em centimetros e milimetros
KM HM dam m dm cm mm
'''
medida = float(input('Digite uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print(' A distância de {}m corresponde a {} cm e {} mm'.format(medida,cm,mm))