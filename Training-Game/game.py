import pygame
from sys import exit

from settings import Settings

class Game:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.screen = pygame.display.get_surface()
        self.display = pygame.Surface(self.settings.display_size)
        self.clock = pygame.time.Clock()
        self.target_fps = self.settings.target_fps
    
    def run(self) -> None:
        while True:
            dt = self.clock.tick(self.target_fps) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            self.display.fill((255,255,255))

            self.screen.blit(pygame.transform.scale2x(self.display), (0,0))
            pygame.display.update()
