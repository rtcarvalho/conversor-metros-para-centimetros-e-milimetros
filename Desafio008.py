print('Desafio008: Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros')

valor1 = int(input('Digite um valor em metros: '))

cm = float(valor1*10)*10
mm = float(valor1*10)*10*10

print('{} metros é equivalente a {} centimetros e a {} milimetros' .format(valor1, cm, mm))