"""Escreva um algoritmo para solicitar ao usuario qe informe o nome, a altura e o peso. apos isso calcule qual o IMC deste usuario (peso/altura²). ao final dos calculos, mostre para o usuario qual o seu IMC"""
nome = input('olá, qual seu nome? ').title()
peso = float(input(f'olá {nome}, qual o seu peso? '))
altura = float(input(f'e qual sua altura {nome}? '))
resultado = float(peso / (altura * altura))
print('muito obrigado, irei checar as informações')
print(f'pronto, {nome} eu calculei seu IMC e deu {resultado:^.2f}!')
