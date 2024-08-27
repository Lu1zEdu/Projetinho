def exibir_tabuleiro(tabuleiro):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(tabuleiro[i][j], end=" ")
        print()

def jogada_valida(tabuleiro, numero, posicao):
    linha, coluna = posicao

    # Verificar a linha
    for i in range(9):
        if tabuleiro[linha][i] == numero and coluna != i:
            return False

    # Verificar a coluna
    for i in range(9):
        if tabuleiro[i][coluna] == numero and linha != i:
            return False

    # Verificar o quadrante 3x3
    caixa_x = coluna // 3
    caixa_y = linha // 3

    for i in range(caixa_y * 3, caixa_y * 3 + 3):
        for j in range(caixa_x * 3, caixa_x * 3 + 3):
            if tabuleiro[i][j] == numero and (i, j) != posicao:
                return False

    return True

def encontrar_vazia(tabuleiro):
    for i in range(9):
        for j in range(9):
            if tabuleiro[i][j] == 0:
                return (i, j)  # linha, coluna
    return None

def resolver_sudoku(tabuleiro):
    encontra = encontrar_vazia(tabuleiro)
    if not encontra:
        return True  # Sudoku resolvido
    else:
        linha, coluna = encontra

    for numero in range(1, 10):  # Corrigido 'em' para 'in'
        if jogada_valida(tabuleiro, numero, (linha, coluna)):
            tabuleiro[linha][coluna] = numero

            if resolver_sudoku(tabuleiro):
                return True

            tabuleiro[linha][coluna] = 0  # Reseta a jogada (retrocesso)

    return False

tabuleiro = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

exibir_tabuleiro(tabuleiro)
resolver_sudoku(tabuleiro)
print("\nSudoku resolvido:\n")
exibir_tabuleiro(tabuleiro)
