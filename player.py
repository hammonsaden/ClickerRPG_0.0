import pygame


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

    def player_draw(self, screen, font):

        # Skill Slots
        self.skill1 = pygame.draw.rect(screen, 'white', (0, 620, 50, 50), 1, border_radius=10)
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
        cast_time = self.skills_dict.get('fireball').get('cast_time')
        self.mana -= self.skills_dict.get('fireball').get('mana_cost')
        self.castbar_total_time = cast_time
        self.castbar_start_time = pygame.time.get_ticks()
        self.is_casting = True

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
