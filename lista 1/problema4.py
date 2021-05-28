#Escreva um porgrama que receba numeros inteiros inverta o valor.
#Exemplo de execução: input: 1234
#                      output4321  
#obs: Não pode usar seq[::-1]
num = int(input('Digite um inteiro de 4 algarismos: '))
dez = num // 1000 # 1
cent = num % 10 # 4 
uni = num % 100
uni = uni // 10 # 3
mil = num // 100
mil = mil % 10 # 2
print(f'Valor invertido: {cent}{uni}{mil}{dez}')