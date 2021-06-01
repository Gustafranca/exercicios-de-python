#Pedro, João e Marcela jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente 
#ao valor que cada um deu para a realização da aposta. Escreva um programa que solicita
#ao usuário quanto cada apostador investiu e o valor do prêmio, e então o programa deve imprimir na
#tela quanto cada um ganharia do prêmio com base no valor investido.


pedro = float(input('Digite o valor que o Pedro apostou: '))
joao = float(input('Digite o valor que o João apostou: '))
marcela = float(input('Digite o valor que a Marcela apostou: '))
premio = float(input('Digite o valor do prêmio: '))

apostatotal = pedro + joao + marcela

p1 = pedro / apostatotal
p2 = joao / apostatotal
p3 = marcela / apostatotal

recebe1 = premio * p1
recebe2 = premio * p2
recebe3 = premio * p3

print(f'Prêmio do Pedro: {recebe1:.2f}')
print(f'Prêmio do João: {recebe2:.2f}')
print(f'Prêmio da Marcela: {recebe3:.2f}')
