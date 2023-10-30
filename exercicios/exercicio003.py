"""Faça um algoritmo que receba do usuario um numero, apos diga se eeste numero está no iintervalo entre 100 e 200"""
numero = int(input('Digite um numero entre 100 e 200:\n>>> '))
if (numero >= 100 and numero <= 200):
    print('o numero que você informou esta entre 100 e 200!')
else:
    if (numero < 100):
        print('o numero que você informou é menos que 100!')
    if (numero > 200):
        print('o numero que você informou é maior que 200!')
