#Escreva um programa que peça ao usuário o valor da sua hora de trabalho, a quantidade de horas
#trabalhadas no mês e calcula a sua folha de pagamento. São descontados do salário o Imposto de
#Renda, que depende do salário bruto (conforme tabela abaixo), e o INSS, que corresponde a 10%
#do salário bruto. O FGTS corresponde a 11% do salário bruto, no entanto o FGTS não é descontado
#do salário, pois é a empresa que deposita. O salário líquido corresponde ao salário bruto menos os
#descontos.
#Salário Bruto Imposto de Renda
#Até R$900 Isento
#Maior que R$900 até R$1500 Desconto de 5%
#Maior que R$1500 até R$2500 Desconto de 10%
#Maior que R$2500 Desconto de 20%


horatrab = float(input('Digite o valor da hora de trabalho: '))
horatrabmes = float(input('Digite a quantidade de horas trabalhadas no mês: '))

salariobruto = horatrab * horatrabmes

print(f'Salário Bruto: {salariobruto:.2f}')
ir = 0
inss = salariobruto * 0.10
fgts = salariobruto * 0.11 #nao desconta do salário

if salariobruto <= 900:
    print(f'IR: {ir:.2f}')
if salariobruto > 900 and salariobruto <= 1500:
    ir = salariobruto * 0.05
    print(f'IR: {ir:.2f}')
if salariobruto > 1500 and salariobruto <= 2500:
    ir = salariobruto * 0.10
    print(f'IR: {ir:.2f}')
if salariobruto > 2500:
    ir = salariobruto * 0.20
    print(f'IR: {ir:.2f}')

print(f'INSS: {inss:.2f}')
print(f'FGTS: {fgts:.2f}')

totaldesconto = ir + inss
salarioliquido = salariobruto - (ir + inss )
print(f'Total de descontos: {totaldesconto:.2f}')
print(f'Salário líquido: {salarioliquido:.2f}')