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

    def main_screen(self, Player, Enemy, Loot_Sys):
        self.invo_isclick = True
        self.shop_isclick = True
        self.display_surface.fill("black")
        self.shop_button = pygame.draw.rect(self.display_surface, 'red', self.shop_button, border_radius=10)
        self.invo_button = pygame.draw.rect(self.display_surface, 'brown', self.invo_button, border_radius=10)


        # Set up
        Enemy.spawn(Player, Loot_Sys)
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

    def inventory_slots_mouseover(self, Player, Loot_Sys, num):
            if Player.inventory[f'slot {num}'] != "empty":
                slot_info = pygame.draw.rect(self.display_surface, "white", (25 + (60 * num), 75, 200, 200), border_radius=10)
                name_info = self.font.render(Player.inventory[f"slot {num}"], True, "Black")
                self.display_surface.blit(name_info, (50 + (60 * num), 75))

                # Get Item Info to load onto the screen
                intel_text = self.font.render("Intellect: ", True, "Black")
                self.display_surface.blit(intel_text, (50 + (60 * num), 100))
                intel_info = self.font.render(str(Loot_Sys.loot_table[Player.inventory[f'slot {num}']]['Intellect']), True, "Black")
                self.display_surface.blit(intel_info, (150 + (60 * num), 100))

                dmg_text = self.font.render("Damage: ", True, "Black")
                self.display_surface.blit(dmg_text, (50 + (60 * num), 130))
                dmg_info = self.font.render(str(Loot_Sys.loot_table[Player.inventory[f'slot {num}']]['Damage']), True, "Black")
                self.display_surface.blit(dmg_info, (150 + (60 * num), 130))

                gold_text = self.font.render("Selling Price: ", True, "Black")
                self.display_surface.blit(gold_text, (50 + (60 * num), 190))
                gold_info = self.font.render(str(Loot_Sys.loot_table[Player.inventory[f'slot {num}']]['Selling Price']) + "g", True, "Black")
                self.display_surface.blit(gold_info, (150 + (60 * num), 190))

                AC_text = self.font.render("AC: ", True, "Black")
                self.display_surface.blit(AC_text, (50 + (60 * num), 160))
                AC_info = self.font.render(str(Loot_Sys.loot_table[Player.inventory[f'slot {num}']]['AC']), True, "Black")
                self.display_surface.blit(AC_info, (150 + (60 * num), 160))

                rarity_text = self.font.render("Rarity: ", True, "Black")
                self.display_surface.blit(rarity_text, (50 + (60 * num), 220))
                rarity_info = self.font.render(str(Loot_Sys.loot_table[Player.inventory[f'slot {num}']]['Rarity']), True, "Black")
                self.display_surface.blit(rarity_info, (150 + (60 * num), 220))
            else:
                pass

    def inventory_screen(self, Player, Loot_Sys):
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


        if self.invo_slot1.collidepoint(pygame.mouse.get_pos()):
            self.inventory_slots_mouseover(Player, Loot_Sys, 1)
        elif self.invo_slot2.collidepoint(pygame.mouse.get_pos()):
            self.inventory_slots_mouseover(Player, Loot_Sys, 2)
        elif self.invo_slot3.collidepoint(pygame.mouse.get_pos()):
            self.inventory_slots_mouseover(Player, Loot_Sys, 3)
        elif self.invo_slot4.collidepoint(pygame.mouse.get_pos()):
            self.inventory_slots_mouseover(Player, Loot_Sys, 4)
        elif self.invo_slot5.collidepoint(pygame.mouse.get_pos()):
            self.inventory_slots_mouseover(Player, Loot_Sys, 5)
        elif self.invo_slot6.collidepoint(pygame.mouse.get_pos()):
            self.inventory_slots_mouseover(Player, Loot_Sys, 6)
        else:
            pass