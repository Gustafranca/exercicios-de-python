#Escreva um  rpograma que converta segundos em horas , minutos e segundos
#Exemplo de execução: input: 3850
#                     output: 1h 4min 10s  
time = int(input('Digite o valor do tempo em segundos: '))
hours = time // 3600
seconds_left = time - (hours*3600)
minutes = seconds_left // 60
seconds_left -= (minutes*60)

print(f'Valor convertido: {hours} h {minutes} min {seconds_left} s')
