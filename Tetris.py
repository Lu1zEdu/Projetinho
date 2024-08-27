import pygame
import random

# Inicializar Pygame
pygame.init()

# Configurações da Tela
largura_tela = 300
altura_tela = 600
tamanho_bloco = 30
colunas = largura_tela // tamanho_bloco
linhas = altura_tela // tamanho_bloco

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
CIANO = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Peças
pecas = [
    [[".....", ".....", "..O..", "..O..", "....."]],
    [[".....", ".....", "..OO.", "..OO.", "....."]],
    [[".....", "..O..", "..O..", "..O..", "....."]],
    [[".....", ".....", ".OO..", "..OO.", "....."]],
    [[".....", ".....", "..OO.", ".OO..", "....."]],
    [[".....", ".....", "..O..", "..OO.", "....."]],
    [[".....", ".....", "..O..", ".OO..", "....."]],
]

cores = [VERMELHO, VERDE, AZUL, AMARELO, CIANO, MAGENTA, BRANCO]


# Função para criar a matriz do tabuleiro
def criar_tabuleiro():
    return [[PRETO for _ in range(colunas)] for _ in range(linhas)]


# Função para desenhar o tabuleiro
def desenhar_tabuleiro(tela, tabuleiro):
    for i in range(linhas):
        for j in range(colunas):
            pygame.draw.rect(
                tela,
                tabuleiro[i][j],
                (j * tamanho_bloco, i * tamanho_bloco, tamanho_bloco, tamanho_bloco),
                0,
            )
    pygame.draw.rect(tela, BRANCO, (0, 0, largura_tela, altura_tela), 5)


# Função para desenhar a grade do tabuleiro
def desenhar_grade(tela):
    for i in range(linhas):
        pygame.draw.line(
            tela, BRANCO, (0, i * tamanho_bloco), (largura_tela, i * tamanho_bloco)
        )
    for j in range(colunas):
        pygame.draw.line(
            tela, BRANCO, (j * tamanho_bloco, 0), (j * tamanho_bloco, altura_tela)
        )


# Função para desenhar uma peça
def desenhar_peca(tela, peca, offset):
    formato = pecas[peca["forma"]][peca["rotacao"] % len(pecas[peca["forma"]])]
    cor = cores[peca["forma"]]

    for i, linha in enumerate(formato):
        for j, coluna in enumerate(linha):
            if coluna == "O":
                pygame.draw.rect(
                    tela,
                    cor,
                    (
                        offset[0] + j * tamanho_bloco,
                        offset[1] + i * tamanho_bloco,
                        tamanho_bloco,
                        tamanho_bloco,
                    ),
                )


# Função para mover a peça para baixo
def mover_peca(peca):
    peca["y"] += 1
    return peca


# Função para gerar uma nova peça
def nova_peca():
    return {
        "forma": random.randint(0, len(pecas) - 1),
        "rotacao": 0,
        "x": colunas // 2 - 2,
        "y": 0,
    }


# Função para verificar colisão
def verificar_colisao(tabuleiro, peca):
    formato = pecas[peca["forma"]][peca["rotacao"] % len(pecas[peca["forma"]])]

    for i, linha in enumerate(formato):
        for j, coluna in enumerate(linha):
            if coluna == "O":
                if (
                    i + peca["y"] >= linhas
                    or j + peca["x"] < 0
                    or j + peca["x"] >= colunas
                    or tabuleiro[i + peca["y"]][j + peca["x"]] != PRETO
                ):
                    return True
    return False


# Função para fixar a peça no tabuleiro
def fixar_peca(tabuleiro, peca):
    formato = pecas[peca["forma"]][peca["rotacao"] % len(pecas[peca["forma"]])]

    for i, linha in enumerate(formato):
        for j, coluna in enumerate(linha):
            if coluna == "O":
                tabuleiro[i + peca["y"]][j + peca["x"]] = cores[peca["forma"]]


# Função para limpar linhas completas
def limpar_linhas(tabuleiro):
    linhas_removidas = 0
    for i in range(linhas):
        if all([tabuleiro[i][j] != PRETO for j in range(colunas)]):
            linhas_removidas += 1
            del tabuleiro[i]
            tabuleiro.insert(0, [PRETO for _ in range(colunas)])
    return linhas_removidas


# Função para exibir a pontuação
def exibir_pontuacao(tela, pontuacao):
    font = pygame.font.Font(None, 36)
    texto = font.render(f"Pontuação: {pontuacao}", True, BRANCO)
    tela.blit(texto, (10, 10))


# Função principal do jogo
def tetris():
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Tetris")
    tabuleiro = criar_tabuleiro()
    peca_atual = nova_peca()
    relogio = pygame.time.Clock()
    game_over = False

    velocidade = 500  # Velocidade inicial (milissegundos por movimento)
    incremento_velocidade = 50  # Aumento da velocidade por nível
    contador_tempo = 0  # Contador para aumentar a velocidade
    pontuacao = 0  # Pontuação inicial

    while not game_over:
        tempo_decorrido = relogio.tick()  # Tempo decorrido desde o último frame
        contador_tempo += tempo_decorrido

        if contador_tempo >= velocidade:
            peca_atual = mover_peca(peca_atual)
            if verificar_colisao(tabuleiro, peca_atual):
                peca_atual["y"] -= 1
                fixar_peca(tabuleiro, peca_atual)
                peca_atual = nova_peca()
                if verificar_colisao(tabuleiro, peca_atual):
                    game_over = True
            contador_tempo = 0

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    peca_atual["x"] -= 1
                    if verificar_colisao(tabuleiro, peca_atual):
                        peca_atual["x"] += 1
                elif evento.key == pygame.K_RIGHT:
                    peca_atual["x"] += 1
                    if verificar_colisao(tabuleiro, peca_atual):
                        peca_atual["x"] -= 1
                elif evento.key == pygame.K_DOWN:
                    peca_atual = mover_peca(peca_atual)
                    if verificar_colisao(tabuleiro, peca_atual):
                        peca_atual["y"] -= 1
                        fixar_peca(tabuleiro, peca_atual)
                        peca_atual = nova_peca()
                elif evento.key == pygame.K_UP:
                    peca_atual["rotacao"] += 1
                    if verificar_colisao(tabuleiro, peca_atual):
                        peca_atual["rotacao"] -= 1

        linhas_completas = limpar_linhas(tabuleiro)
        if linhas_completas > 0:
            pontuacao += linhas_completas * 100  # Adiciona 100 pontos por linha

        tela.fill(PRETO)
        desenhar_tabuleiro(tela, tabuleiro)
        desenhar_grade(tela)
        desenhar_peca(
            tela,
            peca_atual,
            (peca_atual["x"] * tamanho_bloco, peca_atual["y"] * tamanho_bloco),
        )
        exibir_pontuacao(tela, pontuacao)
        pygame.display.update()

        # Aumentar a velocidade conforme o tempo passa
        if velocidade > 100:  # Limite mínimo de velocidade
            velocidade -= incremento_velocidade

    pygame.quit()


if __name__ == "__main__":
    tetris()
