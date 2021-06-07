#O custo total ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor,
# e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com
#a tabela abaixo. Faça um programa que leia o custo de fábrica de um carro novo e imprima na tela o
#custo total ao consumidor.
#Custo de fábrica % do distribuidor % dos impostos
#até R$12.000,00 5% isento
#acima de R$12.000,00 até R$25.000,00 10% 15%
#acima de R$25.000,00 15% 20%

num = float(input('Digite o custo de fábrica: '))

if num <= 12000:
    num = num + (num*0.05)
    print(f'Custo total: {num:.2f}')

elif num > 12000 and num <= 25000:
    num = num + (num*0.10) + (num*0.15)
    print(f'Custo total> {num:.2f}')

elif num > 25000:
    num = num + (num*0.15) + (num*0.20)
    print(f'Custo total: {num:.2f}')