#A redação atual do parágrafo 1o do artigo 40 da Constituição Federal estabelece que um servidor público 
# poderá se aposentar voluntariamente desde que tenha cumprido um tempo mínimo de exercício 2
#no serviço público e atenda uma das seguintes condições:
#• 60 anos de idade e 35 de contribuição, se homem, e 55 anos de idade e 30 de contribuição, se
#mulher; ou,
#• 65 anos de idade, se homem, e 60 anos de idade, se mulher, não importando o tempo de contribuição.
#Faça um programa que receba a idade, o tempo de contribuição e o sexo de um servidor público e
#imprima na tela se esse servidor pode se aposentar ou não. Utilize o caractere "M"para representar o
#sexo masculino e "F"para representar o sexo feminino.


idade = int(input('Digite a idade: '))
tempocont = int(input('Digite o tempo de contribuição: '))
sexo = str(input('Digite o sexo (M/F): '))

sexo = sexo.upper()

if idade > 65 and sexo == 'M':
    print('Pode aposentar')

elif idade > 60 and sexo == 'F':
    print('Pode aposentar')

elif idade >= 60 and tempocont >= 35 and sexo == 'M':
    print('Pode aposentar')

elif idade >= 55 and tempocont >= 30 and sexo == 'F':
    print('Pode aposentar')

else:
    print('Não pode aposentar')