import pygame
import sys
#custom object for copys of walls

class area(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,path_images):
        super().__init__()
        play_load= pygame.image.load('images/playarea.png')
        #crt_load = pygame.image.load('images/crt.png')
        self.image = pygame.transform.scale(play_load, (width,height)).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        #self.image = pygame.transform.scale(crt_load, (width,height)).convert_alpha()
        #self.mask = pygame.mask.from_surface(self.image)
        #self.rect = self.image.get_rect(topleft=(startX,startY))
