import pygame
import random
class Enemy:
    def __init__(self, Player):
        self.level = Player.level
        self.health = self.level * 145
        self.max_health = self.level * 145
        self.enemy_num = None
        self.monster_rect = None
        self.xp_val = 3
        self.monster_spawn = False

    def enemy_gen(self, screen, font):

        if self.enemy_num == 1:
            self.monster_rect = pygame.draw.rect(screen, 'green', (300, 300, 50, 80))
            self.enemy_healthbarbg = pygame.draw.rect(screen, "grey", (225, 250, 200, 20), border_radius=10)
            self.enemy_healthbar = pygame.draw.rect(screen, "red", (225, 250, (self.health / self.max_health) * 200, 20), border_radius=10)
            monster_health = font.render(f"{int(self.health)} / {self.max_health}", True, 'white')
            screen.blit(monster_health, (self.enemy_healthbarbg.centerx - 25, self.enemy_healthbarbg.centery - 5))

        elif self.enemy_num == 2:
            self.monster_rect = pygame.draw.rect(screen, 'red', (300, 300, 50, 80))
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
            self.enemy_num = random.randint(1,2)
            self.health = self.max_health
            self.monster_spawn = True
        elif self.health <= 0:
            self.enemy_num = random.randint(1,2)
            self.health = self.max_health
            self.monster_spawn = True
            Player.xp += self.xp_val
            Player.invo_save()


    def attack(self, dt):
        pass
