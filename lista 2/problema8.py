#Faça um programa que leia duas notas de um aluno, verifique se as notas são válidas e exiba na tela
#a média dessas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0 e 10. Caso uma
#das notas não possua um valor válido, o programa deve exibir a mensagem "Nota inválida". O resultado 
#deve ser exibido com duas casas decimais de precisão.


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    notat = (nota1 + nota2) / 2
    print(f'Média: {notat}')
else:
    print('Nota inválida')