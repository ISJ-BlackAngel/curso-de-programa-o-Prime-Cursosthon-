"""crie uma função que calcula e retorna se 3 valores formam um triangulo. O algoritmo deverá verificar e informar se os lados fornecidos por paramentro formam realmente um triangulo (cada lado é menor que a soma dos outros lados)"""

lado1 = int(input('digite o valor de um lado:\n>>> '))
lado2 = int(input('digite o valor do outro lado:\n>>> '))
lado3 = int(input('digite o valor do outro lado:\n>>> '))

def triangulo(x, y, z):
    triangular = True
    if (not x < y+z):
        triangular = False
    if (not z < y+x):
        triangular = False
    if (not y < x+z):
        triangular = False
    if (triangular):
        print('sim, é um triangulo')
    else:
        print('não é um triangulo')
    return triangular

print(triangulo(lado1, lado2, lado3))
