"""receber do usuario 10 numeros em um vetor e depois exibir os numeros localizados nas posições impares"""

numero = [int(input('informe um numero:\n>>> ')) for x in range(10)]
for i in range(1, len(numero)):
    if (not i%2==0):
        print(f'valor: {numero[i]}, coordenada: {i}')
