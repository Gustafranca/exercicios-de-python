#Escreva um programa que solicita ao usuário um valor de velocidade (v0), um valor de aceleração (a) e um valor de tempo (t ) e o programa imprime na tela a velocidade final e a distância percorrida por um veículo após o intervalo de tempo t , com velocidade inicial igual a v0 e aceleração igual a a. Considere as seguintes fórmulas: 
#Velocidade final: v = v0 + a × t 
#Distâncio percorrida s = v0 + t * at^2 / 2

vo = float(input('Digite o valor da velocidade: '))
a = float(input('Digite o valor da aceleração: '))
t = float(input('Digite o valor do tempo: '))

vf = vo + (a * t)
distancia = vo * t + (a*(t**2)) / 2

print(f'Velocidade final: {vf:.2f}')
print(f'Distância percorrida: {distancia:.2f}')