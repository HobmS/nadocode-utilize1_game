# 0. 기본 초기 설정 (반드시 해야 하는 것들)
import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("HobmS")

# FPS
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지(케릭터, 적군 등), 좌표, 케릭터 속도, 폰트, 게임 시간 등)

# 배경 이미지 불러오기
# background = pygame.image.load("C:\\Users\\ryanp\\Documents\\GitHub\\nadocode-utilize1_game\\blue_background.png")

# 케릭터 불러오기
# character = pygame.image.load("C:\\Users\\ryanp\\Documents\\GitHub\\nadocode-utilize1_game\\character.png")
# character_size = character.get_rect().size 
# character_width = character_size[0] 
# character_height = character_size[1]
# character_x_pos = screen_width/2 - character_width/2
# character_y_pos = screen_height - character_height

# 좌표 설정
# to_x = 0
# to_y = 0

# 케릭터 속도 설정
# character_speed = 0.6

# 적군 설정
# enemy = pygame.image.load("C:\\Users\\ryanp\\Documents\\GitHub\\nadocode-utilize1_game\\enemy.png")
# enemy_size = enemy.get_rect().size 
# enemy_width = enemy_size[0] 
# enemy_height = enemy_size[1]
# enemy_x_pos = screen_width/2 - enemy_width/2
# enemy_y_pos = screen_height/2 - enemy_height/2 

# 폰트 설정
# game_font = pygame.font.Font(None, 40) 

# 게임 시간 설정
# total_time = 10
# start_ticks = pygame.time.get_ticks()

# 이벤트 루프
running = True
while running:
    dt = clock.tick(60) # FPS 설정 (보통 30 또는 60)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    # 게임 종료 이벤트 처리
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

        # 키보드 방향키 이벤트 처리
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         to_x -= character_speed
        #     elif event.key == pygame.K_RIGHT:
        #         to_x += character_speed
        #     elif event.key == pygame.K_UP:
        #         to_y -= character_speed
        #     elif event.key == pygame.K_DOWN:
        #         to_y += character_speed

        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         to_x = 0
        #     elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        #         to_y = 0
    
    # 3. 케릭터 위치 처리
    # character_x_pos += to_x * dt
    # character_y_pos += to_y * dt

    # 경계값 처리 (가로, 세로)
    # if character_x_pos < 0:
    #     character_x_pos = 0
    # elif character_x_pos > screen_width - character_width:
    #     character_x_pos = screen_width - character_width

    # if character_y_pos < 0:
    #     character_y_pos = 0
    # elif character_y_pos > screen_height - character_height:
    #     character_y_pos = screen_height - character_height

    # 4. 충돌 처리: 게임 이미지 간의 충돌 발생 시 반응 처리
    # character_rect = character.get_rect()
    # character_rect.left = character_x_pos
    # character_rect.top = character_y_pos

    # enemy_rect = enemy.get_rect()
    # enemy_rect.left = enemy_x_pos
    # enemy_rect.top = enemy_y_pos
    
    # if character_rect.colliderect(enemy_rect):
    #     print("충돌했어요")
    #     running = False
        
    # 5. 화면에 그리기 (배경화면, 케릭터, 적, 글자 등)
    # screen.blit(background, (0,0))
    # screen.blit(character, (character_x_pos, character_y_pos))
    # screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) 
 
    # elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
    # timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    
    # screen.blit(timer, (10,10))
    
    # if total_time - elapsed_time <= 0:
    #     print("타임아웃")
    #     running = False

    # 매 프레임 별로 새로 그리는 과정 필요 = 반드시 있어야 함 
    pygame.display.update()

# 게임이 종료될 때 바로 종료되면 정 없으니까 딜레이를 주는 방법
# pygame.time.delay(2000) 

# pygame 종료하기: while 문 밖으로 나오면 게임이 종료되도록 하는 부분
pygame.quit()