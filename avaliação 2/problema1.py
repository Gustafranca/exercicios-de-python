# -*- coding: utf-8 -*
#Escreva um programa que solicita ao usuário três números inteiros e
# imprime na tela o número do meio (mediana).

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

d = [a,b,c]
d.sort()

print(f'Mediana: {d[1]}')
