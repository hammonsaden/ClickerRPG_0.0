import pygame
from constants import *
import pickle

class Player:
    def __init__(self):
       
       # Basic Setup
       self.level = 1
       self.intel = 0
       self.gold = 150
       self.xp = 0
       self.xp_needed = int((self.level * 1.35) * 100)

       # Mana
       self.mana = 100
       self.max_mana = int((self.level * 1.10) + (self.intel * 5)) * 100
       self.mana_regen_rate = int(self.intel * 1.10) + 1
       self.last_mana_update_time = pygame.time.get_ticks()

       # Skills
       self.skill1 = None
       self.skill2 = None
       self.skill3 = None
       self.skill4 = None

       # Casting
       self.is_casting = False
       self.castbar_start_time = None
       self.castbar_total_time = None

       # Skills list
       self.current_spells = ['fireball']
       self.skills_dict = {
           'fireball' : {
               'damage' : 25,
               'mana_cost' : 10,
               'cast_time' : 2000,
               'rarity' : 'common'
           }
       }

        # Inventory
       self.inventory = {"slot 1" : "Twisted Wooden Staff", "slot 2" : "empty", "slot 3" : 'empty', 'slot 4' : 'empty', 'slot 5' : 'empty', 'slot 6' : 'empty'}
    def player_draw(self, screen, font):

        # Skill Slots
        if self.current_spells[0] == 'fireball':
            skill1_img = pygame.image.load(FIREBALL_IMG)
            skill1_img_scaled = pygame.transform.scale(skill1_img, (45, 45))
            screen.blit(skill1_img_scaled, (2, 622))
        
        self.skill1 = pygame.draw.rect(screen, 'white', (0, 620, 50, 50), 1, border_radius=10)
        skill1_text = font.render('1', True, 'black')
        screen.blit(skill1_text, (5, 622))
        self.skill2 = pygame.draw.rect(screen, 'white', (55, 620, 50, 50), 1, border_radius=10)
        self.skill3 = pygame.draw.rect(screen, 'white', (110, 620, 50, 50), 1, border_radius=10)
        self.skill4 = pygame.draw.rect(screen, 'white', (165, 620, 50, 50), 1, border_radius=10)

        # Mana Bar
        self.manabar_bg = pygame.draw.rect(screen, "grey", (10, 22, 200, 20), border_radius=10)
        self.manabar = pygame.draw.rect(screen, "blue", (10, 22, max(0, min(self.mana / self.max_mana, 1.0)) * 200, 20), border_radius=10)
        player_mana = font.render(f"{int(self.mana)} / {self.max_mana}", True, 'white')
        screen.blit(player_mana, (self.manabar_bg.centerx - 25, self.manabar_bg.centery - 5))

        # XP Bar
        self.xpbar_bg = pygame.draw.rect(screen, "grey", (5, 2, 690, 15), border_radius=10)
        self.xpbar = pygame.draw.rect(screen, "green", (5, 2, (self.xp / self.xp_needed) * 690, 15), border_radius=10)
        xpbar_text = font.render(f"{int(self.xp)} / {int(self.xp_needed)}", True, "black")
        screen.blit(xpbar_text, (self.xpbar_bg.centerx - 20, self.xpbar_bg.centery - 5))
    def mana_regen(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.last_mana_update_time

        if self.mana < self.max_mana:
            # Calculate how much mana to add based on elapsed time
            mana_to_add = (elapsed_time / 1000) * self.mana_regen_rate

            # Update mana
            self.mana += mana_to_add

            # Update the last update time
            self.last_mana_update_time = current_time
        
    def start_casting_bar(self, num):
        if self.mana >= self.skills_dict['fireball']["mana_cost"]:
            cast_time = self.skills_dict.get('fireball').get('cast_time')
            self.mana -= self.skills_dict.get('fireball').get('mana_cost')
            self.castbar_total_time = cast_time
            self.castbar_start_time = pygame.time.get_ticks()
            self.is_casting = True
        else:
            print("Not Enough Mana to Cast Spell, try again later!")

    def update_cast_bar(self, screen, Enemy):
        if self.castbar_start_time > 0:
            elapsed_time = pygame.time.get_ticks() - self.castbar_start_time

            # Update the cast bar on the screen
            self.draw_cast_bar(screen, Enemy)

    def draw_cast_bar(self, screen, Enemy):
        elapsed_time = pygame.time.get_ticks() - self.castbar_start_time

        bar_width = int((elapsed_time / self.castbar_total_time) * 200)

        self.castbar_bg = pygame.draw.rect(screen, 'grey', (225, 550, 200, 20))
        # self.castbar = pygame.draw.rect(screen, 'yellow', (200, 550, bar_width, 20))

        if bar_width <= 200:
            self.castbar = pygame.draw.rect(screen, 'yellow', (225, 550, bar_width, 20))
        else:
            if Enemy.health > 0:
                Enemy.health -= self.skills_dict.get('fireball').get('damage')
                self.is_casting = False
                self.castbar_start_time = 0
            else:
                Enemy.spawn()

    def invo_load(self):
        try:
            with open("save.pickle", "rb") as file:
                loaded_data = pickle.load(file)
                
                self.level = loaded_data['level']
                self.xp = loaded_data['xp']
                self.intel = loaded_data['intel']
                self.gold = loaded_data['gold']
                self.current_spells = loaded_data['current_spells']
                self.inventory = loaded_data['inventory']

            print(f"Loaded Stats: level : {self.level} xp : {self.xp} intellect : {self.intel} gold : {self.gold} currently equipped spells : {self.current_spells} inventory : {self.inventory}")
        
        except FileNotFoundError:
            print("File is not found. Loading Default Attributes!")
    
    def save_Data(self):
        data = {
            'level' : self.level,
            'xp' : self.xp, 
            'intel' : self.intel,
            'gold' : self.gold,
            'current_spells' : self.current_spells,
            'inventory' : self.inventory
        }
        with open("save.pickle", "wb") as file:
            pickle.dump(data, file)
        print("All Data Saved!")
    
    def add_to_inventory(self, loot_item):
        # Find the next empty slot in the inventory
        empty_slot = next((slot for slot, item in self.inventory.items() if item == "empty"), None)

        if empty_slot is not None:
            # Add the item to the first empty slot
            self.inventory[empty_slot] = loot_item
            print(f"Added {loot_item} to inventory in {empty_slot}.")
            print(self.inventory.values())
        else:
            print("Inventory is full. Cannot add the item.")
