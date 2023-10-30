"""Faça um algoritmo que receba do usuario 10 valores e os organize dentro de um vetor em ordem crescente"""
numero = sorted([int(input('digite um numero: ')) for x in range(10)])
print(', '.join([str(x) for x in numero]))
