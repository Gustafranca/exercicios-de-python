#Uma empresa contrata um encanador pagando R$ 30,00 por dia. Faça um programa que leia o número
#de dias trabalhados pelo encanador e imprima o valor líquido do pagamento que ele deve receber, 
#sabendo que são descontados 8% para imposto de renda.

dias = int(input('Digite a quatidade de dias trabalhados: '))

imposto = (dias * 30) * 0.08
pagamento = (dias * 30) - imposto

print(f'Valor recebido: {pagamento:.2f}')
