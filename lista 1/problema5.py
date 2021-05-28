#Escreva um programa que receba as 3 dimensoes de um retângulo (comprimento, largura, altura) e retorne o volume

comprimento = float(input('Digite o comprimento: '))
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

volume = comprimento * largura * altura

print(f'Volume: {volume:.1f}')

