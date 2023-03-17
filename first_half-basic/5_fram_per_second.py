import pygame

pygame.init()


screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("HobmS")

# FPS
clock = pygame.time.Clock()


background = pygame.image.load("C:\\Users\\ryanp\\Documents\\GitHub\\nadocode-utilize1_game\\blue_background.png")


character = pygame.image.load("C:\\Users\\ryanp\\Documents\\GitHub\\nadocode-utilize1_game\\character.png")
character_size = character.get_rect().size 
character_width = character_size[0] 
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height


to_x = 0
to_y = 0

# 케릭터 이동 속도
character_speed = 0.6

running = True
while running:
    dt = clock.tick(100) # 게임 화면의 초당 프레임 수를 설정

    # print("fps: " + str(clock.get_fps())) # FPS 확인 방법
    # fps가 낮을 경우 케릭터의 움직임이 버벅거림(지극히 정상) + 케릭터 속도가 느려짐(문제 상황)
    # 낮은 fps에서 케릭터가 느려지는 현상을 조정해줘야 함!
    # ex. 케릭터가 1초에 100 이동해야 하는 경우, 10 fps에서는 1초동안 10번 동작 -> 1번 동작 시 10만큼 이동해야 함!


    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x * dt # *dt를 해줌으로써 fps로 인한 속도 차이 보정
    character_y_pos += to_y * dt


    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    

    screen.blit(background, (0,0))
    
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()
