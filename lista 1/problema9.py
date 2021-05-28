#Escreva um programa que recebe um valor em reais, a cotação do dolar, e retorne o valor em dolar

reais = float(input('Digite o valor em reais: '))
cotaçao = float(input('Digite a cotação do dólar: '))

dolar = reais / cotaçao

print(f'Valor em dólar: {dolar:.2f}')