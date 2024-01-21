import pygame
import random
from constants import loot_table

class Enemy:
    def __init__(self, Player):
        self.level = Player.level
        self.health = self.level * 145
        self.max_health = self.level * 145
        self.enemy_num = None
        self.monster_rect = None
        self.xp_val = 3
        self.monster_spawn = False
        self.boss_spawn = False
        self.base_vals = {"health" : self.level * 145, "max_health" : self.level * 145, "xp_val" : 3}
        self.loot_roll = None

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

    def hit(self, state, mouse_pos):
        if state == 'main':
            if self.health > 0:
                self.health -= 2
                return self.monster_rect.collidepoint(mouse_pos)
            else:
                self.monster_spawn = False
                self.spawn()

    def spawn(self, Player):
        if self.monster_spawn == False:
            self.enemy_num = 10 # random.randint(1,10)
            self.health = self.max_health
            self.monster_spawn = True
        elif self.health <= 0:
            self.enemy_num = random.randint(1,10)
            self.loot_drop(Player)
            self.health = self.max_health
            self.monster_spawn = True
            Player.xp += self.xp_val
            Player.invo_save()
        elif self.health <= 0 and self.enemy_num == 10:
            self.boss_spawn = False
            self.loot_drop(Player)
            self.enemy_num = random.randint(1,10)
            self.health = self.max_health
            self.monster_spawn = True
            Player.xp += self.xp_val
            Player.invo_save()

    def attack(self, dt):
        pass

    

    def boss(self):
        if self.boss_spawn == False:
            self.health *= 1.50
            self.max_health *= 1.50
            self.xp_val *=3
            print("boss spawned and health and xp adjusted!")
            self.boss_spawn = True


    def loot_drop(self, Player):
        self.loot_roll = random.randint(1,len(loot_table))
        print(self.loot_roll)
        
        for k,v in Player.inventory.items():
            print(k, v)


