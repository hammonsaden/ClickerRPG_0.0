import pygame
import random

class UI:
    def __init__(self, state):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 20)
        self.state = state
        self.shop_button = None
        self.main_screen_button = None
        self.enemy_num = None
    
    def main_screen(self, Player, Enemy):
        self.display_surface.fill("black")
        self.shop_button = pygame.draw.rect(self.display_surface, 'red', (650, 650, 50, 50), border_radius=10)

        Enemy.spawn(Player)
        Player.player_draw(self.display_surface, self.font)
        Enemy.enemy_gen(self.display_surface, self.font)
        Player.mana_regen()
        if Player.is_casting:
            Player.draw_cast_bar(self.display_surface, Enemy)
            Player.update_cast_bar(self.display_surface, Enemy)

    def shop_screen(self, Player):
        self.display_surface.fill('red')
        self.main_screen_button = pygame.draw.rect(self.display_surface, 'black', (650, 650, 50, 50), border_radius=10)

        header = self.font.render("Shop!", True, 'white')
        self.display_surface.blit(header, (10, 10))

    def inventory_screen(self, Player):
        pass

    def clicked(self, state, mouse_pos):
        if state == "main":
            return self.shop_button.collidepoint(mouse_pos)
        elif state == 'shop':
            return self.main_screen_button.collidepoint(mouse_pos)

        