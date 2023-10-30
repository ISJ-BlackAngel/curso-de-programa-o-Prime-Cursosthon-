# nesse exercicio foi para colocar em pratica a declaração de variavel, e o uso pratico do input
kilometros_percorridos = input('DIGITE QUANTOS KM/H JÁ PERCORREU\n>>> ')
combustivel_gasto = input('DIGITE QUANTOS COMBUSTIVEL FOI GASTO\n>>> ')

media_calculada = int(kilometros_percorridos) / int(combustivel_gasto)

print(f'o consumo medio foi {media_calculada:^.2f}')
