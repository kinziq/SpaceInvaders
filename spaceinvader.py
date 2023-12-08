import pygame
import sys
#custom object for copys of walls
class SpaceInvader(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,path_images):
        super().__init__()
        plr_load= pygame.image.load('images/spaceinvader.png')
        self.image = pygame.transform.scale(plr_load, (width,height)).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.movex = 2
        self.shoot_cooldown = 2000  # Set the cooldown period in milliseconds
        self.last_shot_time = 0
    
    def move(self):
        self.rect.x+=self.movex
    
    def SI_check_hit_X(self,group):
        if pygame.sprite.spritecollide(self, group, False, collided=pygame.sprite.collide_mask):
            return True
        else:
            return    
        
    def SI_collide_X(self):
        self.rect.x-=self.movex
        
        
            
