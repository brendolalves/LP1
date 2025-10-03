import pygame

pygame.init()
LARGURA_TELA = 800
ALTURA_TELA = 600

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("teste 1")
verde = (0,255,0)
cinza = (100,100,100)
pos_x = 370
pos_y = 250
tamanho = 20
rodar = True

while rodar:
    for event in pygame.event.get():
           if event.type == pygame.QUIT:
                rodar = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            pos_x = pos_x - 10
        if event.key == pygame.K_RIGHT:
            pos_x = pos_x +10
        if event.key == pygame.K_UP:
            pos_y = pos_y + 10
        if event.key == pygame.K_DOWN:
            pos_y = pos_y - 10
#preencher a tela com uma cor para limpar frame anterior (importante se houver movimento)
tela.fill(cinza)
#desenhar circulo
pygame.draw.circle(tela, verde, (pos_x,pos_y),tamanho)
pygame.display.flip()

pygame.quit()