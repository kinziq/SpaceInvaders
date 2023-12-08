#Name: Kinz
#Date: 25/10/23
#Purpose: Make a space invaders game
import random
import pygame
import sys
from player import Character
from spaceinvader import SpaceInvader
from playarea import area
from playarea import Background
from bullet import Bullet
from Invaderbullet import Invader_Bullet

pygame.init()

# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

PLAYER_X = 230
PLAYER_Y = 450

INVADER_X = 50
INVADER_Y = 30

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.HWSURFACE)
playersprite = Character(PLAYER_X, PLAYER_Y, 30, 30, 'images/imgoated.png')
Area = area(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, 255)
bg = Background(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, 255)
bullets = Bullet(1000, 1000, 30, 30, 'images/bullet.png')
invader_bullets = Invader_Bullet(1000, 1000, 30, 30, 'images/bullet.png')


Playarea = pygame.sprite.Group()
Player = pygame.sprite.GroupSingle()
Enemy = pygame.sprite.Group()
bullet = pygame.sprite.Group()
invaderbullets = pygame.sprite.Group()
background = pygame.sprite.GroupSingle()
Playarea.add(Area)
Player.add(playersprite)
background.add(bg)

invaders_ROW_1 = [SpaceInvader(INVADER_X + i * 45, INVADER_Y, 30, 20, 'images/spaceinvader.png') for i in range(8)]
invaders_ROW_2 = [SpaceInvader(INVADER_X + i * 45, INVADER_Y + 80, 30, 20, 'images/spaceinvader.png') for i in range(8)]
invaders_ROW_3 = [SpaceInvader(INVADER_X + i * 45, INVADER_Y + 160, 30, 20, 'images/spaceinvader.png') for i in range(8)]
Enemy.add(invaders_ROW_1)
Enemy.add(invaders_ROW_2)
Enemy.add(invaders_ROW_3)
invaderbullets.add(invader_bullets)
bullet.add(bullets)

pygame.display.set_caption("Space Invaders")

# Add a variable to track if the player is hit
is_player_hit = False

def display():
    window.fill((255, 255, 255))  # White background
    background.draw(window)
    Playarea.draw(window)
    Enemy.draw(window)
    Player.draw(window)
    bullet.draw(window)
    invaderbullets.draw(window)

    for invader in Enemy:
        invader.move()

# Add a timer to control the frequency of shooting
shoot_timer = 0
shoot_frequency = 40  # Adjust this value to control shooting frequency
is_invader_shooting = False

while True:
    display()
    playersprite.move(3)
    bullet.update()
    invader_bullets.update()

    for bullet_shot in bullet.sprites():
        bullet_shot.move()
        bullet_shot.check_collision(Enemy)
        bullets.kill()

    if len(Enemy) == 0:
        font = pygame.font.SysFont('Consolas', 30)
        window.blit(font.render("You've Won! GG ez", True, (255, 255, 255)), (100, 250))
        playersprite.kill()
        bullets.kill()

    for invader in Enemy:
        if invader.SI_check_hit_X(Playarea):
            invader.movex = -invader.movex
            invader.rect.y += 40

    # Update the timer
    shoot_timer = (shoot_timer + 1) % shoot_frequency

    if shoot_timer == 0:
        # Randomly choose if an invader should shoot
        should_shoot = random.choice([True, False])

        if should_shoot:
            # Randomly choose one Space Invader to shoot
            shooting_invader = random.choice(Enemy.sprites())
            invader_bullet = Invader_Bullet(shooting_invader.rect.x, shooting_invader.rect.y, 30, 30,'images/bullet.png')
            invaderbullets.add(invader_bullet)

    for invader_bullet in invaderbullets.sprites():
        invader_bullet.move()  # Move the bullets downwards

    # Check collision with the player
    if pygame.sprite.spritecollide(playersprite, invaderbullets, True):
        is_player_hit = True
        playersprite.kill()  # Kill the player when hit
        

    if invader_bullet.rect.y > WINDOW_HEIGHT:
        invader_bullet.kill()  # Remove bullets that go off-screen

    for event in pygame.event.get():
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_SPACE]:
            bullets = Bullet(playersprite.rect.x, playersprite.rect.y, 30, 30, 'images/bullet.png')
            bullet.add(bullets)

        # if user QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if playersprite.plr_check_hit(Playarea):
        playersprite.plr_collide()

    # Display the "You've Lost!" message when the player is hit
    if is_player_hit:
        font = pygame.font.SysFont('Consolas', 20)
        window.blit(font.render("You've Lost!", True, (255, 255, 255)), (100, 250))
        window.blit(font.render("LOL get better or beat it chump!!", True, (255, 255, 255)), (100, 280))
    pygame.display.update()  # update the display
    fpsClock.tick(fps)  # speed of redraw

        
    
    
