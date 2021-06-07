#Faça um programa que leia cinco números inteiros e identifique:
#• O maior valor informado
#• O menor valor informado
#• Quantos números são divisíveis por 3


a = int(input('Digite o primeiro inteiro: '))
b = int(input('Digite o segundo inteiro: '))
c = int(input('Digite o terceiro inteiro: '))
d = int(input('Digite o quarto inteiro: '))
e = int(input('Digite o quinto inteiro: '))

lista = []
lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
lista.append(e)

print(f'Maior: {max(lista)}')
print(f'Menor {min(lista)}')

la = 0

if a % 3 == 0:
    la += 1
if b % 3 == 0:
    la += 1
if c % 3 == 0:
    la += 1
if d % 3 == 0:
    la += 1
if e % 3 == 0:
    la += 1

print(f'Quantidade de divisíveis por 3: {la}')