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
       self.dmg = 0

       # Mana
       self.mana = 100
       self.max_mana = int((self.level * 1.10) + (self.intel * 5)) * 100
       self.mana_regen_rate = int(self.intel * 1.10) + 1
       self.last_mana_update_time = pygame.time.get_ticks()

       # Health
       self.health = 125
       self.max_health = int((self.level * 1.10)) * 150
       self.health_regen_rate = int(self.level * 1.20) + 1
       self.last_health_update_time = pygame.time.get_ticks()

       # Skills
       self.skill1 = None
       self.skill2 = None
       self.skill3 = None
       self.skill4 = None

       # Casting
       self.is_casting = False
       self.castbar_start_time = None
       self.castbar_total_time = None

       # Auto Attack
       self.last_hit_time = 0
       self.hit_interval = 2000

       self.AA_bar_width = 150
       self.AA_bar_height = 10
       self.AA_bar_color = "white"
       self.AA_bar_rect = pygame.Rect(250, 270, self.AA_bar_width,self.AA_bar_height)

       # Skills list
       self.current_spells = ['fireball']
       self.skills_dict = {'fireball' : {'damage' : 25,'mana_cost' : 20,'cast_time' : 2000, 'cd' : 1500, 'required_level' : 1}, 
                        'frost shards' : {'damage' : 15, 'mana_cost' : 10, 'cast_time' : 1000, 'cd' : 1500, 'required_level' : 2},
                        'poison bolt' : {'intial damage' : 5, "dps" : 3, 'duration' : 15000, 'mana_cost' : 15, 'cast_time' : 1500, 'cd' : 3000, 'required_level' : 2},

                        # Level 5 Spells
                        'Flame Blast' : {'damage' : 45, "mana_cost" : 35, 'cast_time' : 1000, "cd" : 10000, 'required_level' : 5},
                        'Frost Nova' : {'damage' : 30, "mana_cost" : 15, 'cast_time' : 1500, 'cd' : 8000, "required_level" : 5},
                        'Toxic Barrage' : {'dps' : 10, 'duration' : 3500, 'mana_cost' : 30, 'cast_time' : 3000, 'required_level' : 5}
       }

        # Inventory
       self.inventory = {"slot 1" : "Twisted Wooden Staff", "slot 2" : "empty", "slot 3" : 'empty', 'slot 4' : 'empty', 'slot 5' : 'empty', 'slot 6' : 'empty', 'slot 7' : 'empty', 'slot 8' : 'empty', 'slot 9' : 'empty', 'slot 10' : 'empty', 'slot 11' : 'empty', 'slot 12' : 'empty'}
       self.currently_equip = {"helm" : "Wooden Bark Helmet", "chest" : "empty", 'legs' : "empty", "feet" : 'empty', 'weapon' : 'empty', 'ring' : 'empty', 'neck' : 'empty'}
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
        self.manabar_bg = pygame.draw.rect(screen, "grey", (10, 45, 200, 20), border_radius=10)
        self.manabar = pygame.draw.rect(screen, "blue", (10, 45, max(0, min(self.mana / self.max_mana, 1.0)) * 200, 20), border_radius=10)
        player_mana = font.render(f"{int(self.mana)} / {self.max_mana}", True, 'white')
        screen.blit(player_mana, (self.manabar_bg.centerx - 25, self.manabar_bg.centery - 5))

        # Health Bar
        self.healthbar_bg = pygame.draw.rect(screen, "grey", (10, 22, 200, 20), border_radius=10)
        self.healthbar = pygame.draw.rect(screen, "red", (10, 22, max(0, min(self.health / self.max_health, 1.0)) * 200, 20), border_radius=10)
        player_health = font.render(f"{int(self.health)} / {self.max_health}", True, "white")
        screen.blit(player_health, (self.healthbar_bg.centerx - 25, self.healthbar_bg.centery - 5))

        # XP Bar
        self.xpbar_bg = pygame.draw.rect(screen, "grey", (5, 2, 690, 15), border_radius=10)
        self.xpbar = pygame.draw.rect(screen, "green", (5, 2, (self.xp / self.xp_needed) * 690, 15), border_radius=10)
        xpbar_text = font.render(f"{int(self.xp)} / {int(self.xp_needed)}", True, "black")
        screen.blit(xpbar_text, (self.xpbar_bg.centerx - 20, self.xpbar_bg.centery - 5))

    def manaandhealth_regen(self):
        current_time = pygame.time.get_ticks()
        elapsed_time1 = current_time - self.last_mana_update_time
        elapsed_time2 = current_time - self.last_health_update_time

        if self.mana < self.max_mana:
            # Calculate how much mana to add based on elapsed time
            mana_to_add = (elapsed_time1 / 1000) * self.mana_regen_rate

            # Update mana
            self.mana += mana_to_add

            # Update the last update time
            self.last_mana_update_time = current_time

        if self.health < self.max_health:
            health_to_add = (elapsed_time2 / 1000) * self.health_regen_rate

            self.health += health_to_add

            self.last_health_update_time = current_time
    
    def reset_fight(self):
        self.health = self.max_health
        self.mana = self.max_mana
        
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

        self.castbar_bg = pygame.draw.rect(screen, 'grey', (225, 550, 200, 20), border_radius=10)
        # self.castbar = pygame.draw.rect(screen, 'yellow', (200, 550, bar_width, 20))

        if bar_width <= 200:
            self.castbar = pygame.draw.rect(screen, 'yellow', (225, 550, bar_width, 20), border_radius=10)
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
                self.currently_equip = loaded_data['currently_equip']

            print(f"Loaded Stats: level : {self.level} xp : {self.xp} intellect : {self.intel} gold : {self.gold} currently equipped spells : {self.current_spells} inventory : {self.inventory} currently equipped items: {self.currently_equip}")
        
        except FileNotFoundError:
            print("File is not found. Loading Default Attributes!")
    
    def save_Data(self):
        data = {
            'level' : self.level,
            'xp' : self.xp, 
            'intel' : self.intel,
            'gold' : self.gold,
            'current_spells' : self.current_spells,
            'inventory' : self.inventory,
            'currently_equip' : self.currently_equip
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
    
    def equip(self, equipment, Loot_Sys):
        if equipment in self.inventory.values():
            slot = Loot_Sys.loot_table[equipment]['slot']

            if slot in self.currently_equip:

                if self.currently_equip[slot]:
                    print("Unequipped item!")
                    self.unequip(slot, Loot_Sys)
                
            self.currently_equip[slot] = equipment
            self.intel += Loot_Sys.loot_table[equipment]['Intellect']
            self.dmg += Loot_Sys.loot_table[equipment]['Damage']
            print(f"Equipped {equipment} in {slot}")
            print(f'intellect {self.intel}')
            print(f'damage: {self.dmg}')

    def unequip(self, slot, Loot_Sys):
        # Unequip the item from the specified slot
        unequipped_item = self.currently_equip[slot]
        if unequipped_item != "empty":
            self.intel -= Loot_Sys.loot_table[unequipped_item]['Intellect']
            self.dmg -= Loot_Sys.loot_table[unequipped_item]['Damage']
            self.currently_equip[slot] = 'empty'
        else:
            print("Slot empty passed!")
            pass
    

    def attack(self, Enemy):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_hit_time >= self.hit_interval:
            Enemy.health -= self.dmg
            print(f"Player hit for {self.dmg} damage!")
            self.last_hit_time = current_time
    
    def draw_AA_bar(self, screen):
        current_time = pygame.time.get_ticks()
        # Draw cast bar background
        pygame.draw.rect(screen, "WHITE", (self.AA_bar_rect.x, self.AA_bar_rect.y, self.AA_bar_width, self.AA_bar_height), border_radius=10)

        # Calculate fill percentage based on remaining cooldown time
        fill_percentage = max(0, (current_time - self.last_hit_time) / self.hit_interval)

        # Draw filled portion of cast bar
        fill_width = int(self.AA_bar_width * fill_percentage)
        fill_rect = pygame.Rect(self.AA_bar_rect.x, self.AA_bar_rect.y, fill_width, self.AA_bar_height, border_radius=10)
        pygame.draw.rect(screen, self.AA_bar_color, fill_rect, border_radius=10)
