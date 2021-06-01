#Escreva um programa que solicita ao usuário um número inteiro e então o programa imprime na tela
#a soma do sucessor de seu triplo com o antecessor de seu dobro.

a = int(input('Digite um numero: '))

b = (a * 3) + 1
c = (a * 2) -1

d = b + c

print(f'Resultado: {d}')
