import pygame
import random


class Enemy:
    def __init__(self, Player):
        self.level = Player.level
        self.health = self.level * 145
        self.max_health = self.level * 145
        self.bosshealth = self.health * 1.50
        self.boss_maxhealth = self.max_health * 1.50
        self.enemy_num = None
        self.monster_rect = None
        self.xp_val = int(self.level * 2 + (1.25))
        self.bossxp_val = self.xp_val * 4
        self.monster_spawn = False
        self.boss_spawn = False
        self.base_vals = {"health" : self.level * 145, "max_health" : self.level * 145, "xp_val" : 3}
        self.loot_roll = None

        # Attacks
        self.last_hit_time = 0
        self.hit_interval = 2000
        self.damage = 10



        # Cast Bar
        self.cast_bar_width = 150
        self.cast_bar_height = 10
        self.cast_bar_color = "Grey"
        self.cast_bar_rect = pygame.Rect(250, 270, self.cast_bar_width,self.cast_bar_height)

    def enemy_gen(self, screen, font):

        if self.enemy_num == 1 or self.enemy_num == 6:
            self.monster_rect = pygame.draw.rect(screen, 'green', (300, 300, 50, 80))
            self.enemy_healthbarbg = pygame.draw.rect(screen, "grey", (225, 250, 200, 20), border_radius=10)
            self.enemy_healthbar = pygame.draw.rect(screen, "red", (225, 250, (self.health / self.max_health) * 200, 20), border_radius=10)
            monster_health = font.render(f"{int(self.health)} / {self.max_health}", True, 'white')
            screen.blit(monster_health, (self.enemy_healthbarbg.centerx - 25, self.enemy_healthbarbg.centery - 5))
        elif self.enemy_num == 2 or self.enemy_num == 7:
            self.monster_rect = pygame.draw.rect(screen, 'red', (300, 300, 50, 80))
            self.enemy_healthbarbg = pygame.draw.rect(screen, "grey", (225, 250, 200, 20), border_radius=10)
            self.enemy_healthbar = pygame.draw.rect(screen, "red", (225, 250, (self.health / self.max_health) * 200, 20), border_radius=10)
            monster_health = font.render(f"{int(self.health)} / {self.max_health}", True, 'white')
            screen.blit(monster_health, (self.enemy_healthbarbg.centerx - 25, self.enemy_healthbarbg.centery - 5))
        elif self.enemy_num == 3 or self.enemy_num == 8:
            self.monster_rect = pygame.draw.rect(screen, 'orange', (300, 300, 50, 80))
            self.enemy_healthbarbg = pygame.draw.rect(screen, "grey", (225, 250, 200, 20), border_radius=10)
            self.enemy_healthbar = pygame.draw.rect(screen, "red", (225, 250, (self.health / self.max_health) * 200, 20), border_radius=10)
            monster_health = font.render(f"{int(self.health)} / {self.max_health}", True, 'white')
            screen.blit(monster_health, (self.enemy_healthbarbg.centerx - 25, self.enemy_healthbarbg.centery - 5))
        elif self.enemy_num == 4 or self.enemy_num == 9:
            self.monster_rect = pygame.draw.rect(screen, 'grey', (300, 300, 50, 80))
            self.enemy_healthbarbg = pygame.draw.rect(screen, "grey", (225, 250, 200, 20), border_radius=10)
            self.enemy_healthbar = pygame.draw.rect(screen, "red", (225, 250, (self.health / self.max_health) * 200, 20), border_radius=10)
            monster_health = font.render(f"{int(self.health)} / {self.max_health}", True, 'white')
            screen.blit(monster_health, (self.enemy_healthbarbg.centerx - 25, self.enemy_healthbarbg.centery - 5))
        elif self.enemy_num == 5:
            self.monster_rect = pygame.draw.rect(screen, 'white', (300, 300, 50, 80))
            self.enemy_healthbarbg = pygame.draw.rect(screen, "grey", (225, 250, 200, 20), border_radius=10)
            self.enemy_healthbar = pygame.draw.rect(screen, "red", (225, 250, (self.health / self.max_health) * 200, 20), border_radius=10)
            monster_health = font.render(f"{int(self.health)} / {self.max_health}", True, 'white')
            screen.blit(monster_health, (self.enemy_healthbarbg.centerx - 25, self.enemy_healthbarbg.centery - 5))
        
        # Boss Spawn!
        elif self.enemy_num == 10:
            self.boss()
            self.monster_rect = pygame.draw.rect(screen, 'gold', (300, 300, 50, 80))
            self.enemy_healthbarbg = pygame.draw.rect(screen, "grey", (225, 250, 200, 20), border_radius=10)
            self.enemy_healthbar = pygame.draw.rect(screen, "red", (225, 250, (self.health / self.max_health) * 200, 20), border_radius=10)
            monster_health = font.render(f"{int(self.health)} / {self.max_health}", True, 'white')
            screen.blit(monster_health, (self.enemy_healthbarbg.centerx - 25, self.enemy_healthbarbg.centery - 5))

    def hit(self, state, mouse_pos, Player):
        if state == 'main':
            if self.health > 0:
                self.health -= Player.dmg
                return self.monster_rect.collidepoint(mouse_pos)
            else:
                self.monster_spawn = False
                self.spawn()

    def spawn(self, Player, Loot_sys):
        # If no enemy is spawned in..
        if self.monster_spawn == False:
            self.enemy_num = 10 # random.randint(1,10)
            self.health = self.max_health
            self.monster_spawn = True
        # If a boss is killed..
        elif self.health <= 0 and self.enemy_num == 10:
            self.boss_spawn = False
            self.enemy_num = random.randint(1,10)
            # self.health = self.max_health
            self.monster_spawn = True
            Player.xp += self.xp_val
            Loot_sys.generate_loot(Player)
            Player.reset_fight()
            # Set the health back to regular amounts
            self.health = self.level * 145
            self.max_health = self.level * 145
            self.xp_val = int(self.level * 2 + (1.25))
            Player.save_Data()
        # If a regular enemy is killed..
        elif self.health <= 0:
            self.enemy_num = random.randint(1,10)
            self.max_health = self.level * 145
            self.xp_val = int(self.level * 2 + (1.25))
            self.health = self.max_health
            self.monster_spawn = True
            Player.xp += self.xp_val
            Player.reset_fight()
            Player.save_Data()
            
    def attack(self, Player):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_hit_time >= self.hit_interval:
            Player.health -= self.damage
            print(f"Player hit for {self.damage} damage!")
            self.last_hit_time = current_time
        
    def draw_cast_bar(self, screen):
        current_time = pygame.time.get_ticks()
        # Draw cast bar background
        pygame.draw.rect(screen, "WHITE", (self.cast_bar_rect.x, self.cast_bar_rect.y, self.cast_bar_width, self.cast_bar_height), border_radius=10)

        # Calculate fill percentage based on remaining cooldown time
        fill_percentage = max(0, (current_time - self.last_hit_time) / self.hit_interval)

        # Draw filled portion of cast bar
        fill_width = int(self.cast_bar_width * fill_percentage)
        fill_rect = pygame.Rect(self.cast_bar_rect.x, self.cast_bar_rect.y, fill_width, self.cast_bar_height, border_radius=10)
        pygame.draw.rect(screen, self.cast_bar_color, fill_rect, border_radius=10)
    

    def boss(self):
        if self.boss_spawn == False:
            self.health = self.bosshealth
            self.max_health = self.boss_maxhealth
            self.xp_val = self.bossxp_val
            print("boss spawned and health and xp adjusted!")
            self.boss_spawn = True



