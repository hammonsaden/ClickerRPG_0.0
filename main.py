import pygame
from constants import *
from ui import UI
from player import Player
from enemy import Enemy
from loot_sys import Loot_Sys

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
        self.Loot_Sys = Loot_Sys()

    def run(self):
        self.Player.invo_load()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        # Inside the run method
                        if self.UI.shop_button.collidepoint(mouse_pos) and self.UI.shop_isclick == True:
                            print("Shop Button Clicked!")
                            self.UI.shopclose_isclick = True
                            self.state = "shop"
                        elif self.UI.invo_button.collidepoint(mouse_pos) and self.UI.invo_isclick == True:
                            print("Inventory Button Clicked!")
                            self.UI.invoclose_isclick = True
                            self.state = "invo"
                        elif self.UI.skilltree_button.collidepoint(mouse_pos) and self.UI.skilltree_isclick == True:
                            print("Skill Tree Button Clicked!")
                            self.UI.skilltreeclose_isclick = True
                            self.state = "skill tree"
                        elif self.Enemy.hit(self.state, mouse_pos, self.Player):
                            pass
                        else:
                            pass

                        # Screen Close Buttons Loop
                        if self.UI.invo_close.collidepoint(mouse_pos) and self.UI.invoclose_isclick == True:
                            self.state = 'main'
                        elif self.UI.shop_close.collidepoint(mouse_pos) and self.UI.shopclose_isclick == True:
                            self.state = 'main'
                        elif self.UI.skilltree_close.collidepoint(mouse_pos) and self.UI.skilltreeclose_isclick == True:
                            self.state = 'main'

                # Spell Handling Event Loop
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        if self.Player.is_casting == False:
                            self.Player.start_casting_bar(1)
                        else:
                            print("Already casting!")
                    if event.key == pygame.K_2:
                        clicked_item = self.Player.inventory['slot 1']
                        self.Player.equip(clicked_item, self.Loot_Sys)
                    
                    if self.state == 'invo':
                        if event.key == pygame.K_e:
                            if self.UI.invo_slot1.collidepoint(pygame.mouse.get_pos()):
                                self.Player.equip(self.Player.inventory['slot 1'], self.Loot_Sys)
                            elif self.UI.invo_slot2.collidepoint(pygame.mouse.get_pos()):
                                self.Player.equip(self.Player.inventory['slot 2'], self.Loot_Sys)
                            elif self.UI.invo_slot3.collidepoint(pygame.mouse.get_pos()):
                                self.Player.equip(self.Player.inventory['slot 3'], self.Loot_Sys)
                            elif self.UI.invo_slot4.collidepoint(pygame.mouse.get_pos()):
                                self.Player.equip(self.Player.inventory['slot 4'], self.Loot_Sys)
                            elif self.UI.invo_slot5.collidepoint(pygame.mouse.get_pos()):
                                self.Player.equip(self.Player.inventory['slot 5'], self.Loot_Sys)
                            elif self.UI.invo_slot6.collidepoint(pygame.mouse.get_pos()):
                                self.Player.equip(self.Player.inventory['slot 6'], self.Loot_Sys)
                            elif self.UI.invo_slot7.collidepoint(pygame.mouse.get_pos()):
                                self.Player.equip(self.Player.inventory['slot 7'], self.Loot_Sys)
                            elif self.UI.invo_slot8.collidepoint(pygame.mouse.get_pos()):
                                self.Player.equip(self.Player.inventory['slot 8'], self.Loot_Sys)
                            elif self.UI.invo_slot9.collidepoint(pygame.mouse.get_pos()):
                                self.Player.equip(self.Player.inventory['slot 9'], self.Loot_Sys)
                            elif self.UI.invo_slot10.collidepoint(pygame.mouse.get_pos()):
                                self.Player.equip(self.Player.inventory['slot 10'], self.Loot_Sys)
                            elif self.UI.invo_slot11.collidepoint(pygame.mouse.get_pos()):
                                self.Player.equip(self.Player.inventory['slot 11'], self.Loot_Sys)
                            elif self.UI.invo_slot12.collidepoint(pygame.mouse.get_pos()):
                                self.Player.equip(self.Player.inventory['slot 12'], self.Loot_Sys)
                            else:
                                pass

            dt = self.clock.tick() / 1000

            if self.state == "main":
                self.UI.main_screen(self.Player, self.Enemy, self.Loot_Sys)
            elif self.state == "shop":
                self.UI.shop_screen(self.Player)
            elif self.state == "invo":
                self.UI.inventory_screen(self.Player, self.Loot_Sys)
            elif self.state == "skill tree":
                self.UI.skilltree_screen(self.Player)

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()