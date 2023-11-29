import pygame

pygame.init()

TAM_TELA = 640
tela = pygame.display.set_mode([TAM_TELA, TAM_TELA])
cor_quadrados_1_hex = "#70a2a3"
cor_quadrados_1 = tuple(int(cor_quadrados_1_hex[i:i+2], 16) for i in (1, 3, 5))

cor_quadrados_2_hex = "#b1e4b9"
cor_quadrados_2 = tuple(int(cor_quadrados_2_hex[i:i+2], 16) for i in (1, 3, 5))

tamanho_fonte = 20
fonte = pygame.font.Font('freesansbold.ttf', tamanho_fonte)
relogio = pygame.time.Clock()
fps = 60

pygame.display.set_caption('PyChess')

brancas = ['torre', 'cavalo', 'bispo', 'rei', 'rainha', 'bispo', 'cavalo', 'torre',
                'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']

brancas_coord = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

pretas = ['torre', 'cavalo', 'bispo', 'rei', 'rainha', 'bispo', 'cavalo', 'torre',
                'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']

pretas_coord = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]


turno = 0
selecao = 10000
movimentos_validos = []

tam = 65
# Adicionando a imagem das pecas brancas
torre_brancas = pygame.transform.scale(pygame.image.load('pecas/torre_brancas.png'), (tam, tam))
cavalo_brancas = pygame.transform.scale(pygame.image.load('pecas/cavalo_brancas.png'), (tam, tam))
bispo_brancas = pygame.transform.scale(pygame.image.load('pecas/bispo_brancas.png'), (tam, tam))
rei_brancas = pygame.transform.scale(pygame.image.load('pecas/rei_brancas.png'), (tam, tam))
rainha_brancas = pygame.transform.scale(pygame.image.load('pecas/rainha_brancas.png'), (tam, tam))
peao_brancas = pygame.transform.scale(pygame.image.load('pecas/peao_brancas.png'), (tam, tam))

# Adicionando a imagem das pecas pretas
torre_pretas = pygame.transform.scale(pygame.image.load('pecas/torre_pretas.png'), (tam, tam))
cavalo_pretas = pygame.transform.scale(pygame.image.load('pecas/cavalo_pretas.png'), (tam, tam))
bispo_pretas = pygame.transform.scale(pygame.image.load('pecas/bispo_pretas.png'), (tam, tam))
rei_pretas = pygame.transform.scale(pygame.image.load('pecas/rei_pretas.png'), (tam, tam))
rainha_pretas = pygame.transform.scale(pygame.image.load('pecas/rainha_pretas.png'), (tam, tam))
peao_pretas = pygame.transform.scale(pygame.image.load('pecas/peao_pretas.png'), (tam, tam))


imagens_brancas = [torre_brancas, cavalo_brancas, bispo_brancas, rei_brancas, rainha_brancas, peao_brancas]
imagens_pretas = [torre_pretas, cavalo_pretas, bispo_pretas, rei_pretas, rainha_pretas, peao_pretas]

pecas = ['torre', 'cavalo', 'bispo', 'rei', 'rainha', 'peao']

def pecas_draw():
    for i in range(len(brancas)):
        index = pecas.index(brancas[i])
        tela.blit(imagens_brancas[index], (brancas_coord[i][0] * 80 + 8, brancas_coord[i][1] * 80 + 8))
        if turno < 2:
            if selecao == i:
                pygame.draw.rect(tela, 'red', [brancas_coord[i][0] * 80, brancas_coord[i][1] * 80, 80, 80], 2)

    for i in range(len(pretas)):
        index = pecas.index(pretas[i])
        tela.blit(imagens_pretas[index], (pretas_coord[i][0] * 80 + 8, pretas_coord[i][1] * 80 + 8))
        if turno >= 2:
            if selecao == i:
                pygame.draw.rect(tela, 'red', [pretas_coord[i][0] * 80, pretas_coord[i][1] * 80, 80, 80], 2)


def tabuleiro_draw(tela, cores):
    tam_quadrado = 640 // 8
    for linha in range(8):
        for coluna in range(8):
            cor = cores[(linha + coluna) % 2]
            #Tabuleiro
            pygame.draw.rect(tela, cor, [coluna * tam_quadrado, linha * tam_quadrado, tam_quadrado, tam_quadrado])

            #Bordas
            pygame.draw.rect(tela, 'black', [coluna * tam_quadrado, linha * tam_quadrado, 2, tam_quadrado])
            pygame.draw.rect(tela, 'black', [coluna * tam_quadrado, linha * tam_quadrado, tam_quadrado, 2])

            pygame.draw.rect(tela, 'black', [642, 0 , 0, 642], 2)
            pygame.draw.rect(tela, 'black', [0, 0 , 642, 642], 2)

def checar_opcoes(pecas, locs, turno):
    lista_movimentos = []
    todos_movimentos = []
    for i in range(len(pecas)):
        loc = locs[i]
        peca = pecas[i]
        if peca == 'peao':
            lista_movimentos = checar_peao(loc, turno)
        """elif peca == 'torre':
            lista_movimentos = checar_torre(loc, turno)
        elif peca == 'cavalo':
            lista_movimentos = checar_cavalo(loc, turno)
        elif peca == 'bispo':
            lista_movimentos = checar_bispo(loc, turno)
        elif peca == 'rainha':
            lista_movimentos = checar_rainha(loc, turno)
        elif peca == 'rei':
            lista_movimentos = checar_rei(loc, turno)"""
        todos_movimentos.append(lista_movimentos)
    return todos_movimentos
           
def checar_peao(posicao, cor):
    lista_movimentos = []
    if cor == 'branca':
        # Mover pra frente 1 casa
        if (posicao[0], posicao[1] + 1) not in brancas_coord and \
           (posicao[0], posicao[1] + 1) not in pretas_coord and posicao[1] < 7:
            lista_movimentos.append((posicao[0], posicao[1] + 1))

        # Mover pra frente 2 casas, caso esteja na posicao inicial
        if (posicao[0], posicao[1] + 2) not in brancas_coord and \
           (posicao[0], posicao[1] + 2) not in pretas_coord and posicao[1] == 1:
            lista_movimentos.append((posicao[0], posicao[1] + 2))

        # Comer uma peca, indo na diagonal
        if (posicao[0] + 1, posicao[1] + 1) in pretas_coord:
            lista_movimentos.append((posicao[0] + 1, posicao[1] + 1))
        if (posicao[0] - 1, posicao[1] + 1) in pretas_coord:
            lista_movimentos.append((posicao[0] - 1, posicao[1] + 1))

    else:
        # Mover pra frente 1 casa
        if (posicao[0], posicao[1] - 1) not in brancas_coord and \
           (posicao[0], posicao[1] - 1) not in pretas_coord and posicao[1] > 0:
            lista_movimentos.append((posicao[0], posicao[1] - 1))

        # Mover pra frente 2 casas, caso esteja na posicao inicial
        if (posicao[0], posicao[1] - 2) not in brancas_coord and \
           (posicao[0], posicao[1] - 2) not in pretas_coord and posicao[1] == 6:
            lista_movimentos.append((posicao[0], posicao[1] - 2))

        # Comer uma peca, indo na diagonal
        if (posicao[0] + 1, posicao[1] - 1) in brancas_coord:
            lista_movimentos.append((posicao[0] + 1, posicao[1] - 1))
        if (posicao[0] - 1, posicao[1] - 1) in brancas_coord:
            lista_movimentos.append((posicao[0] - 1, posicao[1] - 1))

    return lista_movimentos

def checar_movimentos_validos():
    if turno < 2:
        lista_opcoes = opcoes_brancas
    else:
        lista_opcoes = opcoes_pretas
    opcoes_validas = lista_opcoes[selecao]
    return opcoes_validas

def validos_draw(movimentos):
    for i in range(len(movimentos)):
        pygame.draw.circle(tela, 'red', (movimentos[i][0] * 80 + 40, movimentos[i][1] * 80 + 40), 10)


# Loop do jogo
opcoes_pretas = checar_opcoes(pretas, pretas_coord, 'preta')
opcoes_brancas = checar_opcoes(brancas, brancas_coord, 'branca')
rodando = True
while rodando:
    relogio.tick(fps)
    tela.fill(cor_quadrados_1)
    tabuleiro_draw(tela, (cor_quadrados_1, cor_quadrados_2))
    pecas_draw()
    if selecao != 10000:
        movimentos_validos = checar_movimentos_validos()
        validos_draw(movimentos_validos)


    # eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            x_coord = evento.pos[0] // 80
            y_coord = evento.pos[1] // 80
            click_coords = (x_coord, y_coord)
            if turno <= 1:
                if click_coords in brancas_coord:
                    selecao = brancas_coord.index(click_coords)
                    if turno == 0:
                        turno = 1

                if click_coords in movimentos_validos and selecao != 10000:
                    brancas_coord[selecao] = click_coords
                    if click_coords in pretas_coord:
                        peca_preta = pretas_coord.index(click_coords)
                        pretas.pop(peca_preta)
                        pretas_coord.pop(peca_preta)
                    opcoes_pretas = checar_opcoes(pretas, pretas_coord, 'preta')
                    opcoes_brancas = checar_opcoes(brancas, brancas_coord, 'branca')
                    turno = 2
                    selecao = 10000
                    movimentos_validos = []

            if turno > 1:
                if click_coords in pretas_coord:
                    selecao = pretas_coord.index(click_coords)
                    if turno == 2:
                        turno = 3

                if click_coords in movimentos_validos and selecao != 10000:
                    pretas_coord[selecao] = click_coords
                    if click_coords in brancas_coord:
                        peca_branca = brancas_coord.index(click_coords)
                        brancas.pop(peca_branca)
                        brancas_coord.pop(peca_branca)
                    opcoes_pretas = checar_opcoes(pretas, pretas_coord, 'preta')
                    opcoes_brancas = checar_opcoes(brancas, brancas_coord, 'branca')
                    turno = 0
                    selecao = 10000
                    movimentos_validos = []           


    pygame.display.flip()
pygame.quit()