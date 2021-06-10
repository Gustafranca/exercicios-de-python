#Escreva um programa que calcule as raízes da equação de segundo grau, dado os valores de a, b e c:
#ax2 +bx +c = 0
#Lembrando que:
#x = −b ± raiz(∆) / 2a
#∆ = b^2 − 4ac
#A variável a tem que ser diferente de zero. Caso seja igual a zero, imprima a mensagem "Não é uma
#equação quadrática".
#• Se ∆ < 0 , não existe raiz real. Imprima a mensagem "Não existe raiz real".
#• Se ∆ = 0 , existe uma raiz real. Imprima a mensagem "Raiz única"e o valor da raiz.
#• Se ∆ ≥ 0, imprima as duas raízes.



from math import sqrt
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

if a == 0:
    print('Não é uma equação quadrática')
 

delta = (b**2) - (4 * a * c)

x1 = ((-1 * b) + (sqrt(delta))) / (2 * a)
x2 = ((-1 * b) - (sqrt(delta))) / (2 * a)

if delta < 0:
    print('Não existe raiz real')

elif delta == 0:
    print('Raiz única')
    print(f'Raiz: {x1}')
elif delta > 0:
    print(f'Raiz 1: {x1:.2f}')
    print(f'Raiz 2: {x2:.2f}')

