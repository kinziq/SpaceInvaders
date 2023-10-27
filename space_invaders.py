#Name: Kinz
#Date: 25/10/23
#Purpose: Make a space invaders game
import pygame, sys
from player import Character
from spaceinvader import SpaceInvader

pygame.init()

# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

def exit_button():
    sys.exit()

window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame_icon = pygame.image.load('images/SpaceInvadericon.png')
pygame.display.set_icon(pygame_icon)
playersprite=Character(230,450,30,30,'images/imgoated.png')
Invader=SpaceInvader(230,150,30,30,'images/imgoated.png')
InvaderSpeed=4
#Button_1=button.no_background(5, 0, "Arial",20,(0,0,0),(255,0,0),"exit",exit_button)

Player = pygame.sprite.GroupSingle()
Player.add(playersprite)

### The Space Invaders
Enemy = pygame.sprite.Group()
Enemy.add(Invader)


pygame.display.set_caption("Space Invaders")
def display():
    window.fill((255,255,255)) #White background
    Player.draw(window)
    Enemy.draw(window)
    
    
    
    
while True:
    display()
    playersprite.move(3)
    for event in pygame.event.get():
      # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #if playersprite.check_hit():
            #playersprite.collide()
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
    
    
    
    #https://www.pygame.org/docs/tut/MoveIt.html