#Um motorista que ultrapassa a velocidade máxima permitida estará sujeito a uma infração média,
#grave ou gravíssima. Faça um programa que receba dois valores: a velocidade máxima de uma via e
#a velocidade registrada por um radar. Em seguida, o programa deve imprimir na tela se o motorista
#cometeu algum tipo de infração. Considere que as multas são definidas conforme a tabela abaixo:
#Excesso de velocidade sobre a máxima permitida Natureza da infração
#Menor ou igual a velocidade máxima Sem Infração
#Até 20% Infração Média
#Acima de 20% até 50% Infração Grave
#Acima de 50% Infração Gravíssima


vmax = float(input('Digite a velocidade máxima: '))
vregistrado = float(input('Digite a velocidade registrada: '))

if vregistrado <= vmax:
    print('Sem Infração')

elif vregistrado <= vmax + (vmax * 0.20):
    print('Infração Média')

elif vregistrado > vmax + (vmax*0.20) and vregistrado <= vmax + (vmax*0.50):
    print('Infração Grave')

elif vregistrado > vmax + (vmax*0.50):
    print('Infração Gravíssima')
