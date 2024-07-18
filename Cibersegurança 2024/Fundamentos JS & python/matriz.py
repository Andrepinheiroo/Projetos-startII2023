import numpy as np

# Inicializa uma matriz 4x4 com zeros
matriz = np.zeros((4, 4), dtype=int)

# Preenche a matriz com os valores fornecidos pelo usuário
for i in range(4):
    for j in range(4):
        matriz[i][j] = int(input(f"Digite o valor da linha {i+1} e coluna {j+1}: "))
    print()

# Imprime a matriz
for i in range(4):
    for j in range(4):
        print(matriz[i][j], end=' ')
    print() 