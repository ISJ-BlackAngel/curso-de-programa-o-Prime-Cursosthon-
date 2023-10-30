numero = int(input('digite um numero para ver a taboada: '))
print(f'essa é a taboada do numero {numero}:')
for i in range(1, 10+1):
    print(f'{i}x{numero}={int(i*numero)}')
