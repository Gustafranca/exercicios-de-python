#Escreva um programa que solicita ao usuário um número inteiro de 4 algarismos e imprime na tela a
#soma destes algarismos.


num = int(input('Digite um nomero inteiro de 4 algarismos: '))

dez = num // 1000 # 1
cent = num % 10 # 4 
uni = num % 100
uni = uni // 10 # 3
mil = num // 100
mil = mil % 10 # 2

c = dez + cent + uni + mil

print(f'Resultado: {c}')
