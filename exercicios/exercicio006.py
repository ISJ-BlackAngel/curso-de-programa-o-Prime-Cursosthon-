"""desenvolva um algoritmo que peça varias temperaturas ao usuario (quantas ele quiser e sem perguntar antes quantas serão) e quando ele digitar o valor 999 o programa deverar exibir a medida dessas temperaturas e encerrar a execução"""
total = 0
quantidade = 0
while(True):
    temp = float(input('digite uma temperatura, depois digite 999 para ver a media:\n>>> '))
    if (temp == 999):
        print(f'a media total de todas as temperaturas informadas foi de {(total/quantidade):^.2f}')
        print('programa encerrado!')
        break
    else:
        quantidade += 1
        total += temp
    
