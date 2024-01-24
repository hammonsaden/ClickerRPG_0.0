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
        self.skilltree_button = pygame.Rect(550, 650, 50, 50)
        self.skilltree_close = pygame.Rect(650, 0, 50, 50)
        self.invo_close = pygame.Rect(650, 0, 50, 50)
        self.shop_close = pygame.Rect(650, 0, 50, 50)
        self.skilltree_isclick = True
        self.invo_isclick = True
        self.shop_isclick = True
        self.invoclose_isclick = False
        self.shopclose_isclick = False
        self.skilltreeclose_isclick = False
        self.main_screen_button = None
        self.enemy_num = None

    def main_screen(self, Player, Enemy, Loot_Sys):
        self.invo_isclick = True
        self.shop_isclick = True
        self.skilltree_isclick = True

        self.display_surface.fill("black")
        self.shop_button = pygame.draw.rect(self.display_surface, 'red', self.shop_button, border_radius=10)
        self.invo_button = pygame.draw.rect(self.display_surface, 'brown', self.invo_button, border_radius=10)
        self.skilltree_button = pygame.draw.rect(self.display_surface, "light green", self.skilltree_button, border_radius=10)

        # Set up
        Enemy.spawn(Player, Loot_Sys)
        Player.player_draw(self.display_surface, self.font)
        Enemy.enemy_gen(self.display_surface, self.font)
        Player.manaandhealth_regen()
        Enemy.draw_cast_bar(self.display_surface)
        Enemy.attack(Player)
            
        # Casting
        if Player.is_casting:
            Player.draw_cast_bar(self.display_surface, Enemy)
            Player.update_cast_bar(self.display_surface, Enemy)

    def shop_screen(self, Player):
        self.invo_isclick = False
        self.shop_isclick = False
        self.skilltree_isclick = False

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
    
    def equipment_slots_mouseover(self, Player, Loot_Sys, slot, x_pos, y_pos):
        if Player.currently_equip[slot] != "empty":
            # Slot Info
            slot_info = pygame.draw.rect(self.display_surface, "white", (x_pos - 200, y_pos, 200, 200), border_radius=10)
            name_info = self.font.render(Player.currently_equip[slot], True, "Black")
            self.display_surface.blit(name_info, (x_pos - 180, y_pos))

            # Intellect Text
            intel_text = self.font.render("Intellect: ", True, "Black")
            self.display_surface.blit(intel_text, (x_pos - 200, y_pos + 30))
            intel_info = self.font.render(str(Loot_Sys.loot_table[Player.currently_equip[slot]]['Intellect']), True, "Black")
            self.display_surface.blit(intel_info, (x_pos - 100, y_pos + 30))

            # Damage Text
            dmg_text = self.font.render("Damage: ", True, "Black")
            self.display_surface.blit(dmg_text, (x_pos - 200, y_pos + 60))
            dmg_info = self.font.render(str(Loot_Sys.loot_table[Player.currently_equip[slot]]['Damage']), True, "Black")
            self.display_surface.blit(dmg_info, (x_pos - 100, y_pos + 60))

            # Gold Text
            gold_text = self.font.render("Selling Price: ", True, "Black")
            self.display_surface.blit(gold_text, (x_pos - 200, y_pos + 90))
            gold_info = self.font.render(str(Loot_Sys.loot_table[Player.currently_equip[slot]]['Selling Price']) + "g", True, "Black")
            self.display_surface.blit(gold_info, (x_pos - 100, y_pos + 90))
            

            # Armor Class Text
            AC_text = self.font.render("AC: ", True, "Black")
            self.display_surface.blit(AC_text, (x_pos - 200, y_pos + 120))
            AC_info = self.font.render(str(Loot_Sys.loot_table[Player.currently_equip[slot]]['AC']), True, "Black")
            self.display_surface.blit(AC_info, (x_pos - 100, y_pos + 120))


            # Rarity Text
            rarity_text = self.font.render("Rarity: ", True, "Black")
            self.display_surface.blit(rarity_text, (x_pos - 200, y_pos + 150))
            rarity_info = self.font.render(str(Loot_Sys.loot_table[Player.currently_equip[slot]]['Rarity']), True, "Black")
            self.display_surface.blit(rarity_info, (x_pos - 100, y_pos + 150))
        else:
            pass

    def inventory_screen(self, Player, Loot_Sys):
        self.invo_isclick = False
        self.shop_isclick = False
        self.skilltree_isclick = False
    
        self.display_surface.fill("grey")

        self.invo_close = pygame.draw.rect(self.display_surface, "orange", self.invo_close, border_radius=10)
        invo_header = self.shop_font.render("Inventory!", True, 'black')
        self.display_surface.blit(invo_header, (10, 10))

        # Invo Slots
        self.invo_slot1 = pygame.draw.rect(self.display_surface, "black", (0, 50, 50, 50), border_radius=10)
        self.invo_slot2 = pygame.draw.rect(self.display_surface, "black", (60, 50, 50, 50), border_radius=10)
        self.invo_slot3 = pygame.draw.rect(self.display_surface, "black", (120, 50, 50, 50), border_radius=10)
        self.invo_slot4 = pygame.draw.rect(self.display_surface, "black", (180, 50, 50, 50), border_radius=10)
        self.invo_slot5 = pygame.draw.rect(self.display_surface, "black", (240, 50, 50, 50), border_radius=10)
        self.invo_slot6 = pygame.draw.rect(self.display_surface, "black", (300, 50, 50, 50), border_radius=10)
        self.invo_slot7 = pygame.draw.rect(self.display_surface, "black", (0, 110, 50, 50), border_radius=10)
        self.invo_slot8 = pygame.draw.rect(self.display_surface, "black", (60, 110, 50, 50), border_radius=10)
        self.invo_slot9 = pygame.draw.rect(self.display_surface, "black", (120, 110, 50, 50), border_radius=10)
        self.invo_slot10 = pygame.draw.rect(self.display_surface, "black", (180, 110, 50, 50), border_radius=10)
        self.invo_slot11 = pygame.draw.rect(self.display_surface, "black", (240, 110, 50, 50), border_radius=10)
        self.invo_slot12 = pygame.draw.rect(self.display_surface, "black", (300, 110, 50, 50), border_radius=10)


        # Invo Slots Mouseovers
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
        elif self.invo_slot7.collidepoint(pygame.mouse.get_pos()):
            self.inventory_slots_mouseover(Player, Loot_Sys, 7)
        elif self.invo_slot8.collidepoint(pygame.mouse.get_pos()):
            self.inventory_slots_mouseover(Player, Loot_Sys, 8)
        elif self.invo_slot9.collidepoint(pygame.mouse.get_pos()):
            self.inventory_slots_mouseover(Player, Loot_Sys, 9)
        elif self.invo_slot10.collidepoint(pygame.mouse.get_pos()):
            self.inventory_slots_mouseover(Player, Loot_Sys, 10)
        elif self.invo_slot11.collidepoint(pygame.mouse.get_pos()):
            self.inventory_slots_mouseover(Player, Loot_Sys, 11)
        elif self.invo_slot12.collidepoint(pygame.mouse.get_pos()):
            self.inventory_slots_mouseover(Player, Loot_Sys, 12)
        else:
            pass

        # Equipment Slots
        self.helm_slot = pygame.draw.rect(self.display_surface, "black", (500, 70, 50, 50), border_radius=10)
        helm_slotheader = self.font.render("Helm", True, 'black')
        self.display_surface.blit(helm_slotheader, (510, 50))
        self.chest_slot = pygame.draw.rect(self.display_surface, 'black', (500, 160, 50, 50), border_radius=10)
        chest_slotheader = self.font.render("Chest", True, 'black')
        self.display_surface.blit(chest_slotheader, (510, 140))
        self.legs_slot = pygame.draw.rect(self.display_surface, 'black', (500, 240, 50, 50), border_radius=10)
        legs_slotheader = self.font.render("Legs", True, 'black')
        self.display_surface.blit(legs_slotheader, (510, 220))
        self.feet_slot = pygame.draw.rect(self.display_surface, "black", (500, 320, 50, 50), border_radius=10)
        feet_slotheader = self.font.render("Feet", True, 'black')
        self.display_surface.blit(feet_slotheader, (510, 300))
        self.weapon_slot = pygame.draw.rect(self.display_surface, 'black', (420, 160, 50, 50), border_radius=10)
        weapon_slotheader = self.font.render("Weapon", True, 'black')
        self.display_surface.blit(weapon_slotheader, (420, 140))
        self.ring_slot = pygame.draw.rect(self.display_surface, 'black', (580, 220, 50, 50), border_radius=10)
        ring_slotheader = self.font.render("Ring", True, 'black')
        self.display_surface.blit(ring_slotheader, (580, 200))
        self.neck_slot = pygame.draw.rect(self.display_surface, 'black', (580, 140, 50, 50), border_radius=10)
        neck_slotheader = self.font.render("Neck", True, 'black')
        self.display_surface.blit(neck_slotheader, (580, 120))

        if self.helm_slot.collidepoint(pygame.mouse.get_pos()):
            self.equipment_slots_mouseover(Player, Loot_Sys, 'helm', 500, 70)
        elif self.chest_slot.collidepoint(pygame.mouse.get_pos()):
            self.equipment_slots_mouseover(Player, Loot_Sys, 'chest', 500, 160)
        elif self.legs_slot.collidepoint(pygame.mouse.get_pos()):
            self.equipment_slots_mouseover(Player, Loot_Sys, 'legs', 500, 240)
        elif self.feet_slot.collidepoint(pygame.mouse.get_pos()):
            self.equipment_slots_mouseover(Player, Loot_Sys, 'feet', 500, 320)
        elif self.weapon_slot.collidepoint(pygame.mouse.get_pos()):
            self.equipment_slots_mouseover(Player, Loot_Sys, 'weapon', 420, 160)
        elif self.ring_slot.collidepoint(pygame.mouse.get_pos()):
            self.equipment_slots_mouseover(Player, Loot_Sys, 'ring', 580, 220)
        elif self.neck_slot.collidepoint(pygame.mouse.get_pos()):
            self.equipment_slots_mouseover(Player, Loot_Sys, 'neck', 580, 140)
        else:
            pass

    def skilltree_screen(self, Player):
        self.invo_isclick = False
        self.shop_isclick = False
        self.skilltree_isclick = False

        self.display_surface.fill("grey")
        self.skilltree_close = pygame.draw.rect(self.display_surface, "orange", self.skilltree_close, border_radius=10)
        skilltree_header = self.shop_font.render("Skill Tree!", True, 'black')
        self.display_surface.blit(skilltree_header, (10, 10))

