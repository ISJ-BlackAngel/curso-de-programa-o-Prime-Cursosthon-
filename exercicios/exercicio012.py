"""Faça um algoritmo para ler uma matriz 2x3 real edepois gerar e imprimir sua transposta (matriz 3x2 equivalente)
exemplo:
matriz original:
1 2 3
4 5 6
resultado
1 4
2 5
3 6"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
]
# como deveria ficar
# matrixesperada = [
#     [1, 4],
#     [2, 5],
#     [3, 6]
# ]
novamatrix = [[] for x in range(len(matrix[0])]
for col in matrix:
    for pos, ln in enumerate(col):
        novamatrix[pos].append(ln)
print(novamatrix)
