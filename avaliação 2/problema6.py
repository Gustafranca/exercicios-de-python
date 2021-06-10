#Elabore um programa que leia uma data e determine se ela é válida. Ou seja, verifique se o mês está
#entre 1 e 12, e se o dia existe naquele mês. Note que fevereiro tem 29 dias em anos bissextos, e 28 dias
#em anos não bissextos. Além disso, os meses de abril, junho, setembro e novembro possuem 30 dias.
#Seu programa deve ler o dia, mês, e ano da data, nessa ordem. Se a data for válida, exiba a mensagem
#"Data válida". Caso contrário, exiba a mensagem "Data inválida".
#Dica: Um ano é bissexto se ele for múltiplo de 4 e não for múltiplo de 100, ou se ele for múltiplo de 400.

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if  1 <= mes <= 12 and 1 <= dia <= 31 :
    if mes == 2 and 1 <= dia <= 28 and ano % 4 ==0 :
        print('Data válida')
    elif mes == 2 and 1 <= dia <= 28 and ano % 4 != 0 :
        print('Data inválida')    
    elif mes == 2 and 1 <= dia <= 29:
        print('Data válida')
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia == 30:
            print('Data válida')
        if dia > 30:
            print('Data inválida')
    else:
        print('Data válida')    
        