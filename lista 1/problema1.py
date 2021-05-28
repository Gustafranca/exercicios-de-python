#Escreva um programa que solicita ao usuário o raio de uma circunferência e o programa imprime na tela o valor do perímetro e da área dessa circunferência, além do volume da esfera formada por essa circunferência. Considere as seguintes fórmulas: 
#Perímetro = 2 ×π×r 
#Área = π×r 2 
#Volume = 4 ×π× r 
#Observação 1: utilize como valor de π a constante 3.1415 

raio = int(input('Digite o valor do raio da circunferência: '))
raio = float(raio)
pi = 3.1415
perimetro = 2*pi*raio
area = pi * (raio**2)
volume = 4 * pi * (raio*3 / 3)
print(f'Perímetro: {perimetro:.2f} ')
print(f'Área: {area:.2f}')
print(f'Volume: {volume:.2f}')
