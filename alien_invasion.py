import sys
from settings import Settings
import pygame


def run_game():
    # Inicializa o pygame, as configurações e o objeto screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Inicia o laço principal do jogo
    running = True
    while running:
        pygame.init()
        # Obeserva os eventos de teclado e mouse
        for event in pygame.event.get():
            if event.type == quit:
                sys.exit()
        # Redesenha a tela a cada passagem do laço
        screen.fill(ai_settings.bg_color)
        # Deixa a tela mais recente visivel
        pygame.display.flip()


run_game()
