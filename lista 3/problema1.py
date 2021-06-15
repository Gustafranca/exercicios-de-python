#O Supermercado Epa resolveu dar um aumento de salário aos seus colaboradores e lhe contratou para
#desenvolver a solução que calculará os reajustes. Para isso, escreva uma função chamada pagamento
#que recebe como parâmetro o salário atual do colaborador e retorna o salário reajustado de acordo
#com as regras abaixo.

#Salário atual Porcentagem de aumento
#Salários até R$ 280,00 Aumento de 20%
#Maior que R$ 280,00 até R$ 700,00 Aumento de 15%
#Maior que R$ 700,00 até R$ 1500,00 Aumento de 10%
#Maior que R$ 1500,00 Aumento de 5%


def pagamento (salario):
    if salario <= 280: 
        salario = (salario*0.20) + salario
        return salario
    elif salario > 280 and salario <= 700:
        salario = (salario*0.15) + salario
        return salario
    elif salario > 700 and salario <= 1500:
        salario = (salario*0.10) + salario
        return salario
    elif salario > 1500:
        salario = (salario*0.05)
        return salario

