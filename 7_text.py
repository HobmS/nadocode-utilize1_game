import pygame

pygame.init()


screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("HobmS")


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


enemy = pygame.image.load("C:\\Users\\ryanp\\Documents\\GitHub\\nadocode-utilize1_game\\enemy.png")
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0] 
enemy_height = enemy_size[1]
enemy_x_pos = screen_width/2 - enemy_width/2
enemy_y_pos = screen_height/2 - enemy_height/2 

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간 정보 (총 시간을 계산하기 위해 시작 시간 정보가 필요함)
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴


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

    
    character_rect = character.get_rect() 
    character_rect.left = character_x_pos 
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
        



    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) 

    # 타이머 집어넣기: 정해진 시간 내에 목표를 달성해야 하는 게임을 만드는 중이므로, 남은 시간을 표시해주기 위한 타이머를 만드는 것
    # <- 경과 시간을 계산해야 함
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간 단위가 ms이기 때문에 1000으로 나누어서 초(second) 단위로 변환해야 함
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # render함수 사용법: render(출력할 글자, True, 글자 색상)
    screen.blit(timer, (10,10))
    # timer 시간이 0 이하가 되면 게임이 종료되도록 설정하기
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False


    pygame.display.update()

# 종료 전 잠시 대기하도록 설정하는 방법
pygame.time.delay(2000) # 2초 대기

pygame.quit()