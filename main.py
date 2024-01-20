import pygame
from constants import *
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
                        # Inside the run method
                        print(f"Current State: {self.state}")
                        if self.UI.shop_button.collidepoint(mouse_pos) and self.UI.shop_isclick == True:
                            print("Shop Button Clicked!")
                            self.UI.shopclose_isclick = True
                            self.state = "shop"
                        elif self.UI.invo_button.collidepoint(mouse_pos) and self.UI.invo_isclick == True:
                            print("Inventory Button Clicked!")
                            self.Player.invo_load()
                            self.UI.invoclose_isclick = True
                            self.state = "invo"
                        elif self.Enemy.hit(self.state, mouse_pos):
                            pass
                        else:
                            pass


                        if self.UI.invo_close.collidepoint(mouse_pos) and self.UI.invoclose_isclick == True:
                            self.state = 'main'
                        elif self.UI.shop_close.collidepoint(mouse_pos) and self.UI.shopclose_isclick == True:
                            self.state = 'main'

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

            elif self.state == "invo":
                self.UI.inventory_screen(self.Player)

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()