#Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar. Caso
#seja par, imprima a mensagem "Par", caso contrário, imprima a mensagem "Ímpar".


num = int(input('Digite um inteiro: '))

if num % 2 != 0:
    print('Ímpar')
elif num % 2 == 0:
    print('Par')
