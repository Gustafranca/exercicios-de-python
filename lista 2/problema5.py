#Faça um programa que leia um número fornecido pelo usuário. Se esse número for positivo, calcule a
#raiz quadrada do número e exiba o resultado com três casas decimais. Se o número for negativo, exiba
#a mensagem "Número inválido". O programa não deve imprimir nada além disso na tela.

from math import sqrt
num = float(input('Digite um número: '))
if num > 0:
    num = sqrt(num)
    print(f'Resultado: {num:.3f}')
if num == 0:
    print(f'Resultado: 0.000')
elif num < 0:
    print('Número invalido')
    
