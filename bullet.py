import pygame
import sys
#custom object for copys of walls        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,path_images):
        super().__init__()
        self.shot=False
        plr_load= pygame.image.load('images/bullet.png')
        self.image = pygame.transform.scale(plr_load, (width,height)).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.movey = 2
    def move(self):
        self.rect.y-=self.movey
        self.shot=True
        
    def update(self):
        if self.shot:
            self.rect.y-=self.movey
            
    def check_collision(self, enemies):
        collisions = pygame.sprite.spritecollide(self, enemies, True)
        for enemies in collisions:
            self.kill()
