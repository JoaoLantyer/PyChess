import pygame

pygame.init()

# TELA
LARG = 1480
ALT= 640
tela = pygame.display.set_mode([LARG, ALT])

# CORES DO TABULEIRO
cor_quadrados_1_hex = "#70a2a3"
cor_quadrados_1 = tuple(int(cor_quadrados_1_hex[i:i+2], 16) for i in (1, 3, 5))

cor_quadrados_2_hex = "#b1e4b9"
cor_quadrados_2 = tuple(int(cor_quadrados_2_hex[i:i+2], 16) for i in (1, 3, 5))

# TEMPO
relogio = pygame.time.Clock()
fps = 60
frame = 0

pygame.display.set_caption('PyChess')

brancas = ['torre', 'cavalo', 'bispo', 'rainha', 'rei', 'bispo', 'cavalo', 'torre',
                'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']

brancas_coord = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]


pretas = ['torre', 'cavalo', 'bispo', 'rainha', 'rei', 'bispo', 'cavalo', 'torre',
                'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']

pretas_coord = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

turno = 0
selecao = 10000
movimentos_validos = []

tam = 65

# Adicionando a imagem das pecas brancas
torre_brancas = pygame.transform.scale(pygame.image.load('pecas/torre_brancas.png'), (tam, tam))
cavalo_brancas = pygame.transform.scale(pygame.image.load('pecas/cavalo_brancas.png'), (tam, tam))
bispo_brancas = pygame.transform.scale(pygame.image.load('pecas/bispo_brancas.png'), (tam, tam))
rainha_brancas = pygame.transform.scale(pygame.image.load('pecas/rainha_brancas.png'), (tam, tam))
rei_brancas = pygame.transform.scale(pygame.image.load('pecas/rei_brancas.png'), (tam, tam))
peao_brancas = pygame.transform.scale(pygame.image.load('pecas/peao_brancas.png'), (tam, tam))

# Adicionando a imagem das pecas pretas
torre_pretas = pygame.transform.scale(pygame.image.load('pecas/torre_pretas.png'), (tam, tam))
cavalo_pretas = pygame.transform.scale(pygame.image.load('pecas/cavalo_pretas.png'), (tam, tam))
bispo_pretas = pygame.transform.scale(pygame.image.load('pecas/bispo_pretas.png'), (tam, tam))
rainha_pretas = pygame.transform.scale(pygame.image.load('pecas/rainha_pretas.png'), (tam, tam))
rei_pretas = pygame.transform.scale(pygame.image.load('pecas/rei_pretas.png'), (tam, tam))
peao_pretas = pygame.transform.scale(pygame.image.load('pecas/peao_pretas.png'), (tam, tam))

imagens_brancas = [torre_brancas, cavalo_brancas, bispo_brancas, rainha_brancas, rei_brancas, peao_brancas]
imagens_pretas = [torre_pretas, cavalo_pretas, bispo_pretas, rainha_pretas, rei_pretas, peao_pretas]

pecas = ['torre', 'cavalo', 'bispo', 'rainha', 'rei', 'peao']

def pecas_draw_um():
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

def pecas_draw_dois():

    espelho_brancas_coord = [(7 - x, 7 - y) for x, y in brancas_coord]
    espelho_pretas_coord = [(7 - x, 7 - y) for x, y in pretas_coord]

    for i in range(len(brancas)):
        index = pecas.index(brancas[i])
        tela.blit(imagens_brancas[index], (espelho_brancas_coord[i][0] * 80 + 8 + 840, espelho_brancas_coord[i][1] * 80 + 8))
        if turno < 2:
            if selecao == i:
                pygame.draw.rect(tela, 'red', [espelho_brancas_coord[i][0] * 80 + 840, espelho_brancas_coord[i][1] * 80, 80, 80], 2)

    for i in range(len(pretas)):
        index = pecas.index(pretas[i])
        tela.blit(imagens_pretas[index], (espelho_pretas_coord[i][0] * 80 + 8  + 840, espelho_pretas_coord[i][1] * 80 + 8))
        if turno >= 2:
            if selecao == i:
                pygame.draw.rect(tela, 'red', [espelho_pretas_coord[i][0] * 80  + 840, espelho_pretas_coord[i][1] * 80, 80, 80], 2)


def tabuleiros_draw(tela, cores):
    tam_quadrado = 640 // 8

    # Jogador 1
    for linha in range(8):
        for coluna in range(8):
            cor = cores[(linha + coluna) % 2]
            #Tabuleiro
            pygame.draw.rect(tela, cor, [coluna * tam_quadrado, linha * tam_quadrado, tam_quadrado, tam_quadrado])

            #Bordas do Tabuleiro
            pygame.draw.rect(tela, 'black', [coluna * tam_quadrado, linha * tam_quadrado, 2, tam_quadrado])
            pygame.draw.rect(tela, 'black', [coluna * tam_quadrado, linha * tam_quadrado, tam_quadrado, 2])
            pygame.draw.rect(tela, 'black', [0, 0 , 642, 642], 2)

    # Jogador 2
    for linha in range(8):
        for coluna in range(8):
            cor = cores[(linha + coluna) % 2]
            #Tabuleiro
            pygame.draw.rect(tela, cor, [coluna * tam_quadrado + 840, linha * tam_quadrado, tam_quadrado, tam_quadrado])

            #Bordas do Tabuleiro
            pygame.draw.rect(tela, 'black', [coluna * tam_quadrado + 840, linha * tam_quadrado, 2, tam_quadrado])
            pygame.draw.rect(tela, 'black', [coluna * tam_quadrado + 840, linha * tam_quadrado, tam_quadrado, 2])

            
def checar_opcoes(pecas, locs, turno):
    lista_movimentos = []
    todos_movimentos = []
    for i in range(len(pecas)):
        loc = locs[i]
        peca = pecas[i]
        if peca == 'peao':
            lista_movimentos = checar_peao(loc, turno)
        elif peca == 'torre':
            lista_movimentos = checar_torre(loc, turno)
        elif peca == 'cavalo':
            lista_movimentos = checar_cavalo(loc, turno)
        elif peca == 'bispo':
            lista_movimentos = checar_bispo(loc, turno)
        elif peca == 'rainha':
            lista_movimentos = checar_rainha(loc, turno)
        elif peca == 'rei':
            lista_movimentos = checar_rei(loc, turno)
        todos_movimentos.append(lista_movimentos)
    return todos_movimentos


def checar_peao(posicao, cor):
    lista_movimentos = []
    if cor == 'branca':
        # Mover pra frente 1 casa
        if (posicao[0], posicao[1] - 1) not in pretas_coord and \
           (posicao[0], posicao[1] - 1) not in brancas_coord and posicao[1] > 0:
            lista_movimentos.append((posicao[0], posicao[1] - 1))

            # Mover pra frente 2 casas, caso esteja na posicao inicial
            if (posicao[0], posicao[1] - 2) not in pretas_coord and \
            (posicao[0], posicao[1] - 2) not in brancas_coord and posicao[1] == 6:
                lista_movimentos.append((posicao[0], posicao[1] - 2))

        # Comer uma peca, indo na diagonal
        if (posicao[0] + 1, posicao[1] - 1) in pretas_coord:
            lista_movimentos.append((posicao[0] + 1, posicao[1] - 1))
        if (posicao[0] - 1, posicao[1] - 1) in pretas_coord:
            lista_movimentos.append((posicao[0] - 1, posicao[1] - 1))

    else:
        # Mover pra frente 1 casa
        if (posicao[0], posicao[1] + 1) not in pretas_coord and \
           (posicao[0], posicao[1] + 1) not in brancas_coord and posicao[1] < 7:
            lista_movimentos.append((posicao[0], posicao[1] + 1))

            # Mover pra frente 2 casas, caso esteja na posicao inicial
            if (posicao[0], posicao[1] + 2) not in pretas_coord and \
            (posicao[0], posicao[1] + 2) not in brancas_coord and posicao[1] == 1:
                lista_movimentos.append((posicao[0], posicao[1] + 2))

        # Comer uma peca, indo na diagonal
        if (posicao[0] + 1, posicao[1] + 1) in brancas_coord:
            lista_movimentos.append((posicao[0] + 1, posicao[1] + 1))
        if (posicao[0] - 1, posicao[1] + 1) in brancas_coord:
            lista_movimentos.append((posicao[0] - 1, posicao[1] + 1))

    return lista_movimentos


def checar_torre(posicao, cor):
    lista_movimentos = []
    if cor == 'branca':
         # Torres brancas

        lista_aliados = brancas_coord
        lista_inimigos = pretas_coord
    else:
        #Torres pretas

        lista_aliados = pretas_coord
        lista_inimigos = brancas_coord

    for i in range(4): # as 4 direcoes
        caminho = True
        sequencia = 1

        # baixo
        if i == 0:
            x = 0
            y = 1

        # cima    
        elif i == 1:
            x = 0
            y = -1

        # direita
        elif i == 2:
            x = 1
            y = 0

        # esquerda
        else:
            x = -1
            y = 0 
        while caminho:
            if (posicao[0] + (sequencia * x), posicao[1] + (sequencia * y)) not in lista_aliados and \
            0 <= posicao[0] + (sequencia * x) <= 7 and 0 <= posicao[1] + (sequencia * y) <= 7:
                lista_movimentos.append((posicao[0] + (sequencia * x), posicao[1] + (sequencia * y)))
                if (posicao[0] + (sequencia * x), posicao[1] + (sequencia * y)) in lista_inimigos:
                    caminho = False
                sequencia += 1
            else:
                caminho = False

    return lista_movimentos


def checar_cavalo(posicao, cor):
    lista_movimentos = []
    
    if cor == 'branca':
         # Cavalos brancos
        lista_aliados = brancas_coord
    else:
        #Cavalos pretos
        lista_aliados = pretas_coord


    alvos = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
    for i in range(8):
        alvo = (posicao[0] + alvos[i][0], posicao[1] + alvos[i][1])
        if alvo not in lista_aliados and 0 <= alvo[0] <= 7 and 0 <= alvo[1] <= 7:
            lista_movimentos.append(alvo)


    return lista_movimentos


def checar_bispo(posicao, cor):
    lista_movimentos = []

    if cor == 'branca':
         # Bispos brancos

        lista_aliados = brancas_coord
        lista_inimigos = pretas_coord
    else:
        # Bispos pretos

        lista_aliados = pretas_coord
        lista_inimigos = brancas_coord

    for i in range(4): # as 4 diagonais
        caminho = True
        sequencia = 1

        # nordeste
        if i == 0:
            x = 1
            y = -1

        # noroeste   
        elif i == 1:
            x = -1
            y = -1

        # sudeste
        elif i == 2:
            x = 1
            y = 1

        # sudoeste
        else:
            x = -1
            y = 1 
        while caminho:
            if (posicao[0] + (sequencia * x), posicao[1] + (sequencia * y)) not in lista_aliados and \
            0 <= posicao[0] + (sequencia * x) <= 7 and 0 <= posicao[1] + (sequencia * y) <= 7:
                lista_movimentos.append((posicao[0] + (sequencia * x), posicao[1] + (sequencia * y)))
                if (posicao[0] + (sequencia * x), posicao[1] + (sequencia * y)) in lista_inimigos:
                    caminho = False
                sequencia += 1
            else:
                caminho = False   

    return lista_movimentos


def checar_rainha(posicao, cor):
    lista_movimentos = []

    # Adicionando os movimentos de torre a rainha
    lista_movimentos_torre = checar_torre(posicao,cor)

    for i in range(len(lista_movimentos_torre)):
        lista_movimentos.append(lista_movimentos_torre[i])

    # Adicionando os movimentos de bispo a rainha
    lista_movimentos_bispo = checar_bispo(posicao, cor)

    for i in range(len(lista_movimentos_bispo)):
        lista_movimentos.append(lista_movimentos_bispo[i])

    return lista_movimentos

def checar_rei(posicao, cor):
    lista_movimentos = []
    if cor == 'branca':
         # Torres brancas

        lista_aliados = brancas_coord
    else:
        #Torres pretas

        lista_aliados = pretas_coord

    alvos = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
    for i in range(8):
        alvo = (posicao[0] + alvos[i][0], posicao[1] + alvos[i][1])
        if alvo not in lista_aliados and 0 <= alvo[0] <= 7 and 0 <= alvo[1] <= 7:
            lista_movimentos.append(alvo)

    return lista_movimentos

def xeque_draw():
    if turno < 2:
        if 'rei' in brancas:
            rei_index = brancas.index('rei')
            rei_loc = brancas_coord[rei_index]
            for i in range(len(opcoes_pretas)):
                if rei_loc in opcoes_pretas[i]:
                    if frame < 30:
                        pygame.draw.rect(tela, 'dark red', [rei_loc[0] * 80 + 1, rei_loc[1] * 80 + 1, 80, 80], 5)

                        espelhado_x = 7 - rei_loc[0]
                        espelhado_y = 7 - rei_loc[1]

                        pygame.draw.rect(tela, 'dark red', [espelhado_x * 80 + 1 + 840, espelhado_y * 80 + 1, 80, 80], 5)

    else:
        if 'rei' in pretas:
            rei_index = pretas.index('rei')
            rei_loc = pretas_coord[rei_index]
            for i in range(len(opcoes_brancas)):
                if rei_loc in opcoes_brancas[i]:
                    if frame < 30:
                        pygame.draw.rect(tela, 'dark red', [rei_loc[0] * 80 + 1, rei_loc[1] * 80 + 1, 80, 80], 5)

                        espelhado_x = 7 - rei_loc[0]
                        espelhado_y = 7 - rei_loc[1]

                        pygame.draw.rect(tela, 'dark red', [espelhado_x * 80 + 1 + 840, espelhado_y * 80 + 1, 80, 80], 5)


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

        x_espelhado = 7 - movimentos[i][0]
        y_espelhado = 7 - movimentos[i][1]

        pygame.draw.circle(tela, 'red', (x_espelhado * 80 + 40 + 840, y_espelhado * 80 + 40), 10)


# Loop do jogo
opcoes_brancas = checar_opcoes(brancas, brancas_coord, 'branca')
opcoes_pretas = checar_opcoes(pretas, pretas_coord, 'preta')
rodando = True
while rodando:
    relogio.tick(fps)
    if frame < 60:
        frame += 1
    else:
        frame = 0
    tela.fill(cor_quadrados_1)
    tabuleiros_draw(tela, (cor_quadrados_1, cor_quadrados_2))
    pecas_draw_um()
    pecas_draw_dois()
    xeque_draw()
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

            if evento.pos[0] > 840:
                x_coord = (evento.pos[0] - 840) // 80
                y_coord = evento.pos[1] // 80
                x_coord = 7 - x_coord
                y_coord = 7 - y_coord

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