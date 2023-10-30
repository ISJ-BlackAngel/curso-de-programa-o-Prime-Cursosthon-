"""dados um capital, uma taxa de juros (em porcentagem) mensal e um periodo em meses, informe o montante ao final de cada mes. o programa deve funcionar como a seguir:
juros: 10%
capital: 100.00
Periodo: 3

1ª mes: RS 110.00
2ª mes: RS 121.00
"""

juros = 10
capital = 100.00
periodo = 3

print(f'''
Juros: {juros}%
Capital Inicial: R${capital:^.2f}
Periodo: {periodo}
''')
for i in range(periodo):
    print(f'{i+1} mes +R${float(10 * capital / 100):^.2f} R${(capital+float(10 * capital / 100)):^.2f}')
    capital += float(10 * capital / 100)
print(f'''
Juros: {juros}%
Capital Final: R${capital:^.2f}
Periodo: {periodo}
''')
