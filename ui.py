import pygame
import random

class UI:
    def __init__(self, state):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 20)
        self.shop_font = pygame.font.Font(None, 35)
        self.state = state
        self.shop_button = pygame.Rect(650, 650, 50, 50)
        self.invo_button = pygame.Rect(600, 650, 50, 50)
        self.invo_close = pygame.Rect(650, 0, 50, 50)
        self.shop_close = pygame.Rect(650, 0, 50, 50)
        self.invo_isclick = True
        self.shop_isclick = True
        self.invoclose_isclick = False
        self.shopclose_isclick = False
        self.main_screen_button = None
        self.enemy_num = None

    def main_screen(self, Player, Enemy):
        self.invo_isclick = True
        self.shop_isclick = True
        self.display_surface.fill("black")
        self.shop_button = pygame.draw.rect(self.display_surface, 'red', self.shop_button, border_radius=10)
        self.invo_button = pygame.draw.rect(self.display_surface, 'brown', self.invo_button, border_radius=10)


        # Set up
        Enemy.spawn(Player)
        Player.player_draw(self.display_surface, self.font)
        Enemy.enemy_gen(self.display_surface, self.font)
        Player.mana_regen()
            
        # Casting
        if Player.is_casting:
            Player.draw_cast_bar(self.display_surface, Enemy)
            Player.update_cast_bar(self.display_surface, Enemy)

    def shop_screen(self, Player):
        self.invo_isclick = False
        self.shop_isclick = False

        self.display_surface.fill('red')
        self.main_screen_button = pygame.draw.rect(self.display_surface, 'black', (650, 650, 50, 50), border_radius=10)

        header = self.shop_font.render("Shop!", True, 'white')
        self.display_surface.blit(header, (10, 10))
        self.shop_close = pygame.draw.rect(self.display_surface, "orange", self.shop_close, border_radius=10)

    def inventory_screen(self, Player):
        self.invo_isclick = False
        self.shop_isclick = False
    
        self.display_surface.fill("grey")

        self.invo_close = pygame.draw.rect(self.display_surface, "orange", self.shop_close, border_radius=10)
        invo_header = self.shop_font.render("Inventory!", True, 'black')
        self.display_surface.blit(invo_header, (10, 10))

        # Row 1
        self.invo_slot1 = pygame.draw.rect(self.display_surface, "black", (0, 50, 50, 50), border_radius=10)
        self.invo_slot2 = pygame.draw.rect(self.display_surface, "black", (60, 50, 50, 50), border_radius=10)
        self.invo_slot3 = pygame.draw.rect(self.display_surface, "black", (120, 50, 50, 50), border_radius=10)
        self.invo_slot4 = pygame.draw.rect(self.display_surface, "black", (180, 50, 50, 50), border_radius=10)
        self.invo_slot5 = pygame.draw.rect(self.display_surface, "black", (240, 50, 50, 50), border_radius=10)
        self.invo_slot6 = pygame.draw.rect(self.display_surface, "black", (300, 50, 50, 50), border_radius=10)