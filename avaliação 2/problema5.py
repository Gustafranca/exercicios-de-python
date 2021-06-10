#Uma empresa vende o mesmo produto para quatro estados diferentes. Cada estado possui uma taxa
#de imposto sobre o produto, como indicado na tabela abaixo. Faça um programa em que o usuário
#entre com o valor e a sigla do estado destino do produto e o programa retorne o preço final do produto acrescido do imposto do estado em que ele será vendido. Caso o estado inserido não seja um
#dos estados válidos, imprima a mensagem "Estado inválido".
#Estado Taxa de imposto
#       MG 7%
#       SP 12%
#       RJ 15%
#       MS 8%

valor = float(input('Digite o valor do produto: '))
estado = str(input('Digite o estado: '))

estado.upper()

if estado == 'MG':
    vf = (valor * 0.07) + valor
    print(F'Valor final: {vf:.2f}')
elif estado == 'SP':
    vf = (valor * 0.12) + valor
    print(f'Valor final: {vf:.2f}')
elif estado == 'RJ':
    vf = (valor * 0.15) + valor
    print(f'Valor final {vf}')
elif estado == 'MS':
    vf = (valor * 0.08) + valor
    print(f'Valor final: {vf}')

else: 
    print('Estado inválido')
    


