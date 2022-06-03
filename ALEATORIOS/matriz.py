def determinante_triangular(mat):
    det = 1
    n = len(mat)
    detFinal = []
    for i in range(n):
        detFinal.append(mat[i][i])
    for idx in range(0,len(detFinal)):
        det = det * detFinal[idx]
    return det
matriz =[
[1, 0, 1, 2],
[0, 3, 1, 3],
[0, 0, 1, 5],
[0, 0, 0, 7],
]
determinante = determinante_triangular(matriz)
print(determinante)