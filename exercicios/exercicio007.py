"""Escreva um algoritmo que le um numero desconhecido de valores um de cada vez e conta quantos dele estão em cada um dos intervalos [0, 25], [26, 50], [51, 75], [76, 100]. O programa deve fechar quando o usuario digitar um valor negativo."""
num0a25 = 0
num26a50 = 0
num51a75 = 0
num76a100 = 0
numero = 0
while(numero >= 0):
    numero = int(input('digite um numero:\n>>>> '))
    if (numero >= 0 and numero <= 25):
        num0a25 += 1
    if (numero >= 26 and numero <= 50):
        num26a50 += 1
    if (numero >= 51 and numero <= 75):
        num51a75 += 1
    if (numero >= 76 and numero <= 100):
        num76a100 += 1
print(f'''
{num0a25} foram entre 0 a 25
{num26a50} foram entre 26 a 50
{num51a75} foram entre 51 a 75
{num76a100} foram entre 76 a 100
''')
    
