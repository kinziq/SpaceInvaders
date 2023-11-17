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
Invader2=SpaceInvader(Invaderlocx+45,Invaderlocy,50,30,'images/spaceinvader.png')
Invader3=SpaceInvader(Invaderlocx+90,Invaderlocy,50,30,'images/spaceinvader.png')
Invader4=SpaceInvader(Invaderlocx+135,Invaderlocy,50,30,'images/spaceinvader.png')
Invader5=SpaceInvader(Invaderlocx+180,Invaderlocy,50,30,'images/spaceinvader.png')
Invader6=SpaceInvader(Invaderlocx+225,Invaderlocy,50,30,'images/spaceinvader.png')
Invader7=SpaceInvader(Invaderlocx+270,Invaderlocy,50,30,'images/spaceinvader.png')
bullets=Bullet(1000,1000,30,30,'images/bullet.png')
#Button_1=button.no_background(5, 0, "Arial",20,(0,0,0),(255,0,0),"exit",exit_button)



Playarea = pygame.sprite.Group()
Player = pygame.sprite.GroupSingle()
Enemy = pygame.sprite.Group()
bullet=pygame.sprite.Group()
Playarea.add(bg)
Player.add(playersprite)
Enemy.add(Invader,Invader2,Invader3,Invader4,Invader5,Invader6)
bullet.add(bullets)

pygame.display.set_caption("Space Invaders")
def display():
    window.fill((255,255,255)) #White background
    Playarea.draw(window)
    Enemy.draw(window)
    Player.draw(window)
    bullet.draw(window)
    Invader.move()
    Invader2.move()
    Invader3.move()
    Invader4.move()
    Invader5.move()
    Invader6.move()
    Invader7.move()
    # Invader4.move()
    
    
while True:
    display()
    playersprite.move(3)    
    
    
    
    # if pygame.sprite.spritecollide(bg, Enemy, False, collided=pygame.sprite.collide_mask):
    #     row+=1
    bullet.update()
    for event in pygame.event.get():
        
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_SPACE]:
            bullets=Bullet(playersprite.rect.x,playersprite.rect.y,30,30,255)
            bullet.add(bullets)
            bullet.draw(window)
            bullets.move()
            
        # if user QUIT then the screen will close
    if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    
    
    if Invader.SI_check_hit_X(Playarea):
            Invader.movex=-Invader.movex
            Invader.rect.y+=40
            Invader2.movex=-Invader2.movex
            Invader2.rect.y+=40
            Invader3.movex=-Invader3.movex
            Invader3.rect.y+=40
            Invader4.movex=-Invader4.movex
            Invader4.rect.y+=40
            Invader5.movex=-Invader5.movex
            Invader5.rect.y+=40
            
    if Invader5.SI_check_hit_X(Playarea):
            Invader.movex=-Invader.movex
            Invader.rect.y+=40
            Invader2.movex=-Invader2.movex
            Invader2.rect.y+=40
            Invader3.movex=-Invader3.movex
            Invader3.rect.y+=40
            Invader4.movex=-Invader4.movex
            Invader4.rect.y+=40
            Invader5.movex=-Invader5.movex
            Invader5.rect.y+=40
    if playersprite.plr_check_hit(Playarea):
            playersprite.plr_collide()
        
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
        
    
    
