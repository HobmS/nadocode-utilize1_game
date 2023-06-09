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


character_speed = 0.6

# Enenmy 케릭터
enemy = pygame.image.load("C:\\Users\\ryanp\\Documents\\GitHub\\nadocode-utilize1_game\\enemy.png")
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0] 
enemy_height = enemy_size[1]
enemy_x_pos = screen_width/2 - enemy_width/2
enemy_y_pos = screen_height/2 - enemy_height/2 # enemy 생성 위치 = 화면 중앙

running = True
while running:
    dt = clock.tick(60) 


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
    
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt


    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트: enemy와 케릭터가 충돌 시 게임이 종료되도록 설정
    character_rect = character.get_rect() # character_rect라는 character의 위치에 대한 정보를 가진 변수 생성
    character_rect.left = character_x_pos # 사용자의 조작에 의해 변형된 character_rect 정보를 새로 가져오기 위한 과정임
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
        



    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # enemy 화면에 그리기

    pygame.display.update()

pygame.quit()
