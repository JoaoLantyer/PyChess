import pygame

pygame.init()

tela = pygame.display.set_mode([630, 630])
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

tam = 60


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
        tela.blit(imagens_brancas[index], (brancas_coord[i][0] * 80 + 5, brancas_coord[i][1] * 80 + 5))

    for i in range(len(pretas)):
        index = pecas.index(pretas[i])
        tela.blit(imagens_pretas[index], (pretas_coord[i][0] * 80 + 5, pretas_coord[i][1] * 80 + 5))

def tabuleiro_draw(tela, cores):
    tam_quadrado = 635 // 8
    for linha in range(8):
        for coluna in range(8):
            cor = cores[(linha + coluna) % 2]
            pygame.draw.rect(tela, cor, [coluna * tam_quadrado, linha * tam_quadrado, tam_quadrado, tam_quadrado])
   

rodando = True
while rodando:
    relogio.tick(fps)
    tela.fill(cor_quadrados_1)
    tabuleiro_draw(tela, (cor_quadrados_1, cor_quadrados_2))
    pecas_draw()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    pygame.display.flip()
pygame.quit()