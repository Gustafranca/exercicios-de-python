#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os valores dos reajustes. Faça um programa que
#receba o salário de um colaborador, calcula o reajuste segundo a tabela abaixo, e exibe o valor do
#aumento e o valor do novo salário.
#Salário atual Porcentagem de aumento
#Salários até R$ 280,00 Aumento de 20%
#Maior que R$ 280,00 até R$ 700,00 Aumento de 15%
#Maior que R$ 700,00 até R$ 1500,00 Aumento de 10%
#Maior que R$ 1500,00 Aumento de 5%


salario = float(input('Digite o valor do salário: '))
ajuste = 0

if salario <= 280:
    ajuste = salario * 0.20
    salario = salario + (salario * 0.20)
    print(f'Valor do aumento: {ajuste:.2f}')
    print(f'Novo salário: {salario:.2f}')

elif salario > 280 and salario <= 700:
    ajuste = salario * 0.15
    salario = salario + (salario * 0.15)
    print(f'Valor do aumento: {ajuste:.2f}')
    print(f'Novo salário: {salario:.2f}')

elif salario > 700 and  salario <= 1500:
    ajuste = salario * 0.10
    salario = salario + (salario * 0.10)
    print(f'Valor do aumento: {ajuste:.2f}')
    print(f'Novo salário: {salario:.2f}')

elif salario > 1500:
    ajuste = salario * 0.05
    salario = salario + (salario * 0.05)
    print(f'Valor do aumento: {ajuste:.2f}')
    print(f'Novo salário: {salario:.2f}')