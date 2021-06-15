#Faça um programa para determinar o tipo de um triângulo. Para isso, crie duas funções:
#1. Uma chamada verifica_triangulo, que recebe como parâmetros três lados de um triângulo
#e retorna True se os lados formarem um triângulo, ou False caso negativo
#2. Outra chamada tipo_triangulo, que recebe como parâmetros três lados de um triângulo e
#retorna uma das três strings a seguir: Equilátero, Isósceles ou Escaleno. Ou seja, a função
#retorna o tipo do triângulo formado pelos três lados informados
#Algumas dicas:
#• Para verificar se é um triângulo, confira se os lados obedecem a desigualdade triangular: z <
#x + y e y < x + z e x < y + z.
#Tipo do triângulo Lados
#Triângulo Equilátero 3 lados iguais
#Triângulo Isósceles 2 lados iguais
#Triângulo Escaleno 3 lados diferentes

def verifica_triangulo(x,y,z):
    if z < x + y and y < x + z and x < y + z:
        return True
    else:
        return False


def tipo_triangulo(x,y,z):
    if x == y and y == z:
        return 'Triângulo Equiçátero'
    elif x == y or x == z or y == z:
        return 'Trinângulo Isósceles'
    elif x != y and x != z and y != z:
        return 'Triângulo Escaleno'
    else:
        return'Não é um triângulo'