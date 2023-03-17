import pygame

pygame.init()


screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("HobmS")


background = pygame.image.load("C:\\Users\\ryanp\\Documents\\GitHub\\nadocode-utilize1_game\\blue_background.png")


character = pygame.image.load("C:\\Users\\ryanp\\Documents\\GitHub\\nadocode-utilize1_game\\character.png")
character_size = character.get_rect().size 
character_width = character_size[0] 
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0


running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: # 키를 누른 경우
            if event.key == pygame.K_LEFT: # 왼쪽 방향키를 누른 경우, 케릭터를 왼쪽으로 이동
                to_x -= 5
            elif event.key == pygame.K_RIGHT: # 오른쪽 방향키를 누른 경우, 케릭터를 오른쪽으로 이동
                to_x += 5
            elif event.key == pygame.K_UP: #  위쪽 방향키를 누른 경우, 케릭터를 위로 이동
                to_y -= 5
            elif event.key == pygame.K_DOWN: # 아래쪽  방향키를 누른 경우, 케릭터를 아래로 이동
                to_y += 5

        if event.type == pygame.KEYUP: # 키에서 손을 땐 경우
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x
    character_y_pos += to_y

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    

    screen.blit(background, (0,0))
    
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

# pygame 종료
pygame.quit()