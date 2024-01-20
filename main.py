import pygame
from settings import *
from ui import UI
from player import Player
from enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Clicker RPG")
        self.clock = pygame.time.Clock()
        self.state = 'main'
        self.UI = UI(self.state)
        self.Player = Player()
        self.Enemy = Enemy(self.Player)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.UI.clicked(self.state, mouse_pos):
                            if self.state == 'main':
                                self.state = 'shop'
                            elif self.state == 'shop':
                                self.state = 'main'
                        elif self.Enemy.hit(self.state, mouse_pos):
                            pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        if self.Player.is_casting == False:
                            self.Player.start_casting_bar(1)
                        else:
                            print("Already casting!")
            dt = self.clock.tick() / 1000

            if self.state == "main":
                self.UI.main_screen(self.Player, self.Enemy)

            elif self.state == "shop":
                self.UI.shop_screen(self.Player)

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()