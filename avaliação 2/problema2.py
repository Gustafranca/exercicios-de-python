#Escreva um programa que solicita ao usuário três valores x, y e z e verifica se eles podem ser os
#comprimentos do lado de um triângulo. Caso eles formem um triângulo, imprima se o mesmo é
#um triângulo equilátero, isósceles ou escaleno. Caso contrário, imprima a mensagem "Não é um
#triângulo". Considere o que segue:
#• Para verificar se é um triângulo, confira se os lados obedecem a desigualdade triangular: 
#z < x + y e y < x + z e x < y + z.
#Tipo do triângulo Lados
#Triângulo Equilátero 3 lados iguais
#Triângulo Isósceles 2 lados iguais
#Triângulo Escaleno 3 lados diferentes

x = float(input('Digite o comprimento do priemiro lado: '))
y = float(input('Digite o comprimento do segndo lado: '))
z = float(input('Digite o comprimento do terceiro lado: '))

if z < x + y and y < x + z and x < y + z:
    if x == y and y == z:
        print('Triângulo Equiçátero')
    elif x == y or x == z or y == z:
        print('Trinângulo Isósceles')
    elif x != y and x != z and y != z:
        print('Triângulo Escaleno')
else:
    print('Não é um triângulo')