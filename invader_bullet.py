import pygame
import sys

class Invader_Bullet(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,path_images):
        super().__init__()
        self.shot=False
        bullet_load= pygame.image.load('images/bullet.png')
        self.image = pygame.transform.scale(bullet_load, (width,height)).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.movey = 7
    def move(self):
        self.rect.y+=self.movey
        self.shot=True
        
    def invaderupdate(self):
        if self.shot:
            self.rect.y-=self.movey
            
    def check_collision(self, enemies):
        collisions = pygame.sprite.spritecollide(self, enemies, True)
        for enemies in collisions:
            self.kill()
