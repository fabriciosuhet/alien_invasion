import sys
import pygame


def run_game():
    # Inicializa o jogo e cria um ojbeto para a tela
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Alien Invasion")
    # Inicia o laço principal do jogo
    running = True
    while running:
        pygame.init()
        # Obeserva os eventos de teclado e mouse
        for event in pygame.event.get():
            if event.type == quit:
                sys.exit()
        pygame.display.flip()


run_game()
