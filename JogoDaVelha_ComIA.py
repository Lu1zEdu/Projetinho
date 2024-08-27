def inicializar_tabuleiro():
    return [[' ' for _ in range(3)] for _ in range(3)]

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)
def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas, colunas e diagonais
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or \
           all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False

def verificar_empate(tabuleiro):
    return all([cell != ' ' for row in tabuleiro for cell in row])


import random


def jogada_ia(tabuleiro, jogador_ia, jogador_humano):
    # Verificar se a IA pode vencer
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                tabuleiro[i][j] = jogador_ia
                if verificar_vitoria(tabuleiro, jogador_ia):
                    return
                tabuleiro[i][j] = ' '

    # Verificar se o jogador humano pode vencer na próxima jogada e bloquear
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                tabuleiro[i][j] = jogador_humano
                if verificar_vitoria(tabuleiro, jogador_humano):
                    tabuleiro[i][j] = jogador_ia
                    return
                tabuleiro[i][j] = ' '

    # Se nenhuma das condições acima for satisfeita, faça uma jogada aleatória
    while True:
        i, j = random.randint(0, 2), random.randint(0, 2)
        if tabuleiro[i][j] == ' ':
            tabuleiro[i][j] = jogador_ia
            break


def jogo_da_velha():
    tabuleiro = inicializar_tabuleiro()
    jogador_humano = 'X'
    jogador_ia = 'O'
    turno = jogador_humano

    while True:
        exibir_tabuleiro(tabuleiro)

        if turno == jogador_humano:
            linha = int(input("Escolha a linha (0, 1, 2): "))
            coluna = int(input("Escolha a coluna (0, 1, 2): "))
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = jogador_humano
                if verificar_vitoria(tabuleiro, jogador_humano):
                    exibir_tabuleiro(tabuleiro)
                    print("Você venceu!")
                    break
                turno = jogador_ia
            else:
                print("Posição já ocupada! Tente novamente.")
        else:
            jogada_ia(tabuleiro, jogador_ia, jogador_humano)
            if verificar_vitoria(tabuleiro, jogador_ia):
                exibir_tabuleiro(tabuleiro)
                print("Você perdeu!")
                break
            turno = jogador_humano

        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break


jogo_da_velha()
