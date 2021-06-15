#Crie uma função chamada peso_ideal que receba como parâmetros a altura em metros e o sexo de
#uma pessoa e calcule o seu peso ideal em kg, utilizando as seguintes fórmulas:
#• Sexo feminino: (62.1 ·h)−44.7
#• Sexo masculino: (72.7 ·h)−58
#onde h é a altura em metros.
#O sexo será informado com um caractere; "F" para feminino e "M" para masculino.


def peso_ideal(altura, sexo):
    altura.upper()
    if sexo == 'F':
        peso = (62.1 * altura) - 44.7
        return peso
    elif sexo == 'M':
        peso = (72.7 * altura) - 58
        return peso