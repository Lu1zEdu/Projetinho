import pygame
import random

# Inicializar Pygame
pygame.init()

# Configurações da Tela
largura_tela = 500  # Aumentado para incluir a área das próximas peças
altura_tela = 600
tamanho_bloco = 30
colunas = largura_tela // tamanho_bloco
linhas = altura_tela // tamanho_bloco
largura_jogo = 300  # Largura do jogo em si, sem a área das próximas peças
colunas_jogo = largura_jogo // tamanho_bloco

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
    return [[PRETO for _ in range(colunas_jogo)] for _ in range(linhas)]

# Função para desenhar o tabuleiro
def desenhar_tabuleiro(tela, tabuleiro):
    for i in range(linhas):
        for j in range(colunas_jogo):
            pygame.draw.rect(
                tela,
                tabuleiro[i][j],
                (j * tamanho_bloco, i * tamanho_bloco, tamanho_bloco, tamanho_bloco),
                0,
            )
    pygame.draw.rect(tela, BRANCO, (0, 0, largura_jogo, altura_tela), 5)

# Função para desenhar a grade do tabuleiro
def desenhar_grade(tela):
    for i in range(linhas):
        pygame.draw.line(
            tela, BRANCO, (0, i * tamanho_bloco), (largura_jogo, i * tamanho_bloco)
        )
    for j in range(colunas_jogo):
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
        "x": colunas_jogo // 2 - 2,
        "y": 0,
    }

# Função para verificar colisão
def verificar_colisao(tabuleiro, peca, rotacao=None):
    if rotacao is None:
        rotacao = peca["rotacao"]
    formato = pecas[peca["forma"]][rotacao % len(pecas[peca["forma"]])]

    for i, linha in enumerate(formato):
        for j, coluna in enumerate(linha):
            if coluna == "O":
                if (
                    i + peca["y"] >= linhas
                    or j + peca["x"] < 0
                    or j + peca["x"] >= colunas_jogo
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
        if all([tabuleiro[i][j] != PRETO for j in range(colunas_jogo)]):
            linhas_removidas += 1
            del tabuleiro[i]
            tabuleiro.insert(0, [PRETO for _ in range(colunas_jogo)])
    return linhas_removidas

# Função para exibir a pontuação
def exibir_pontuacao(tela, pontuacao):
    font = pygame.font.Font(None, 36)
    texto = font.render(f"Pontuação: {pontuacao}", True, BRANCO)
    tela.blit(texto, (largura_jogo + 10, 10))

# Função para desenhar as próximas peças
def desenhar_proximas_pecas(tela, proximas_pecas):
    for i, peca in enumerate(proximas_pecas):
        offset_x = largura_jogo + 10
        offset_y = 60 + i * 100  # Espaçamento entre as peças
        desenhar_peca(
            tela,
            peca,
            (offset_x, offset_y),
        )

# Função principal do jogo
def tetris():
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Tetris")
    tabuleiro = criar_tabuleiro()

    peca_atual = nova_peca()
    proximas_pecas = [nova_peca() for _ in range(3)]  # Armazenar as próximas 3 peças

    relogio = pygame.time.Clock()
    game_over = False

    velocidade = 300  # Velocidade inicial aumentada (milissegundos por movimento)
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
                peca_atual = proximas_pecas.pop(0)  # Pega a próxima peça
                proximas_pecas.append(nova_peca())  # Adiciona uma nova peça à fila
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
                        peca_atual = proximas_pecas.pop(0)
                        proximas_pecas.append(nova_peca())
                        if verificar_colisao(tabuleiro, peca_atual):
                            game_over = True
                    contador_tempo = 0
                elif evento.key == pygame.K_UP:  # Usar a tecla SETA PARA CIMA para girar a peça
                    rotacao_anterior = peca_atual["rotacao"]
                    peca_atual["rotacao"] += 1
                    if verificar_colisao(tabuleiro, peca_atual):
                        peca_atual["rotacao"] = rotacao_anterior

        # Limpar linhas e atualizar a pontuação
        linhas_removidas = limpar_linhas(tabuleiro)
        if linhas_removidas > 0:
            pontuacao += linhas_removidas * 100  # Incrementa a pontuação
            contador_tempo = 0  # Reseta o contador de tempo ao limpar uma linha
            if velocidade > 100:  # Aumentar a velocidade, mas mantendo um limite mínimo
                velocidade -= incremento_velocidade

        # Desenhar tudo
        tela.fill(PRETO)
        desenhar_tabuleiro(tela, tabuleiro)
        desenhar_peca(tela, peca_atual, (peca_atual["x"] * tamanho_bloco, peca_atual["y"] * tamanho_bloco))
        desenhar_grade(tela)
        exibir_pontuacao(tela, pontuacao)
        desenhar_proximas_pecas(tela, proximas_pecas)  # Desenhar as próximas peças

        pygame.display.update()

    pygame.quit()


# Rodar o jogo
tetris()
