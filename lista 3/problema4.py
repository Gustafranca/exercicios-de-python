#Um posto está vendendo combustíveis de acordo com os descontos a seguir:
#• Álcool ("a")
#– até 20 litros, desconto de 3% por litro
#– acima de 20 litros, desconto de 5% por litro
#• Gasolina ("g")
#– até 20 litros, desconto de 4% por litro
#– acima de 20 litros, desconto de 6% por litro
#Escreva uma função chamada calcula_valor que recebe como parâmetros o preço do litro de combustível, a quantidade de litros abastecidos e o tipo de combustível utilizado ("a"ou "g") e retorna o
#valor a ser pago de acordo com as regras acima.

def calcula_valor(preçol, labastecido, tipocombustivel):
    tipocombustivel.lower()
    if tipocombustivel == 'a':
        if labastecido <= 20:
            pagar = ((preçol* 0.03) - preçol) * labastecido
            return pagar
        elif labastecido > 20:
            pagar = ((preçol* 0.05) - preçol) * labastecido
    if tipocombustivel == 'g':
        if labastecido <= 20:
            pagar = ((preçol* 0.04) - preçol) * labastecido
        elif labastecido > 20:
            pagar = ((preçol* 0.06) - preçol) * labastecido


