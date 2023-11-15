#Name: Kinz
#Date: 25/10/23
#Purpose: Make a space invaders game
import pygame, sys
from player import Character
from spaceinvader import SpaceInvader
from playarea import area
from bullet import Bullet

pygame.init()

# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

def exit_button():
    sys.exit()

Invaderlocx = 50
Invaderlocy = 20

Playerlocx= 230
Playerlocy= 450


window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
playersprite=Character(Playerlocx,Playerlocy,30,30,'images/imgoated.png')
bg=area(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT,255)
Invader=SpaceInvader(Invaderlocx,Invaderlocy,50,30,'images/spaceinvader.png')
bullets=Bullet(250,250,30,30,'images/bullet.png')
#Button_1=button.no_background(5, 0, "Arial",20,(0,0,0),(255,0,0),"exit",exit_button)



Playarea = pygame.sprite.Group()
Player = pygame.sprite.GroupSingle()
Enemy = pygame.sprite.Group()
bullet=pygame.sprite.Group()
Playarea.add(bg)
Player.add(playersprite)
Enemy.add(Invader)
bullet.add(bullets)

pygame.display.set_caption("Space Invaders")
def display():
    window.fill((255,255,255)) #White background
    Playarea.draw(window)
    Enemy.draw(window)
    Player.draw(window)
    bullet.draw(window)
    Invader.move()
    
    
while True:
    display()
    playersprite.move(3)    
    
    
    
    # if pygame.sprite.spritecollide(bg, Enemy, False, collided=pygame.sprite.collide_mask):
    #     row+=1
    bullet.update()
    for event in pygame.event.get():
        
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_SPACE]:
            bullets=Bullet(playersprite.rect.x,playersprite.rect.y,30,30)
            bullet.add(bullets)
            bullets.move()
            bullet.draw(window)
            
        # if user QUIT then the screen will close
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if Invader.SI_check_hit_X(Playarea):
            Invader.movex=-Invader.movex
            Invader.rect.y+=20
            
        if playersprite.plr_check_hit(Playarea):
            playersprite.plr_collide()
        
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
        
    
    
