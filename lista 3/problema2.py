#Você foi contratado para realizar o cálculo da folha de pagamento de uma empresa. Para isso, escreva
#uma função chamada pagamento que recebe como parâmetros o valor da hora trabalhada e a quantidade de horas trabalhadas e retorna o salário após os descontos do Imposto de Renda (IR), conforme
#as regras abaixo.
#Salário bruto Porcentagem de desconto do IR
#Salários até até R$ 900,00 Isento de desconto do IR
#Maior que R$ 900,00 até R$ 1500,00 Desconto de 5%
#Maior que R$ 1500,00 até R$ 2500,00 Desconto de 10%
#Maior que R$ 2500,00 Desconto de 20%

def pagamento(valorh, quntidadeh):
    #salrio geral

    salario = valorh * quntidadeh

    #desocnto ir 

    if salario < 900:
        return salario
    elif salario > 900 and salario <= 1500:
        salario = (salario * 0.05) - salario
        return salario
    elif salario > 1500 and salario <= 2500:
        salario = (salario * 0.10) - salario
        return salario
    elif salario > 2500:
        salario = (salario * 0.20) - salario
        return salario

