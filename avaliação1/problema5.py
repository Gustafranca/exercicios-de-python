#Escreva um programa para ajudar vendedores de uma loja de roupas. O seu programa deverá ler o
#valor de uma compra e a partir dele exibir na tela as seguintes informações:
#• O preço com 10% de desconto, para pagamentos à vista;
#• O valor de cada parcela caso o preço seja parcelado em 6x (sem juros);
#• A comissão do vendedor, caso o pagamento seja à vista (5% sobre valor com o desconto de 10%);
#• A comissão do vendedor, caso o pagamento seja parcelado (5% sobre o valor integral).
#Esses quatro valores devem ser exibidos nessa ordem, um por linha. O seu programa não deve 
# imprimir mais nada além disso.



a = float(input('Digite o valor da compra: '))
desconto = a - (a * 0.1) 
parcela = a / 6
comisavista = (desconto * 0.05)
comisaparcelado = (a * 0.05)

print(f'Valor com desconto: {desconto:.2f}')
print(f'Valor da parcela: {parcela:.2f}')
print(f'Comissão do vendedor (à vista): {comisavista:.2f}')
print(f'Comissão do vendedor (parcelado): {comisaparcelado:.2f}')
