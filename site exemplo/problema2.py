vo = float(input('Digite o valor da velocidade: '))
a = float(input('Digite o valor da aceleração: '))
t = float(input('Digite o valor do tempo: '))

vf = vo + (a * t)
distancia = vo * t + (a*(t**2)) / 2

print(f'Velocidade final: {vf:.2f}')
print(f'Distância percorrida: {distancia:.2f}')