import pygame
from random import *

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Dodge Dungs")

clock = pygame.time.Clock()

background = pygame.image.load("C:\\Users\\ryanp\\Documents\\GitHub\\nadocode-utilize1_game\\blue_background.png")

character = pygame.image.load("C:\\Users\\ryanp\\Documents\\GitHub\\nadocode-utilize1_game\\character.png")
character_size = character.get_rect().size 
character_width = character_size[0] 
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height

to_x = 0

character_speed = 0.6

dung = pygame.image.load("C:\\Users\\ryanp\\Documents\\GitHub\\nadocode-utilize1_game\\enemy.png")
dung_size = dung.get_rect().size 
dung_width = dung_size[0] 
dung_height = dung_size[1]
dung_x_pos = uniform(0, screen_width - dung_width)
dung_y_pos = 0 

dung_speed = 0.6

game_font = pygame.font.Font(None, 40) 

total_time = 15
start_ticks = pygame.time.get_ticks()

running = True
while running:
    dt = clock.tick(30)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    
    character_x_pos += to_x * dt
    dung_y_pos += dung_speed * dt
    
    if dung_y_pos > screen_height - dung_height:
        dung_y_pos = 0
        dung_x_pos = uniform(0, screen_width - dung_width)

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    dung_rect = dung.get_rect()
    dung_rect.left = dung_x_pos
    dung_rect.top = dung_y_pos
    
    if character_rect.colliderect(dung_rect):
        print("누가 내 머리 위에 똥 쌌어 ㅠㅠ")
        running = False
        
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(dung, (dung_x_pos, dung_y_pos)) 
 
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    
    screen.blit(timer, (10,10))
    
    if total_time - elapsed_time <= 0:
        print("휴~ 냄새")
        running = False

    pygame.display.update()

pygame.time.delay(2000) 

pygame.quit()