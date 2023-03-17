import pygame

pygame.init()


screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("HobmS")

# 배경 이미지 불러오기 - 이미지 파일에서 'copy path(파일 경로 복사)' 후, 탈출문자 처리를 위해 \를 \\ 또는 /로 수정 후 사용할 것! 
# 뒤에서 blit, pygame.display.update도 추가해야 배경이 추가됨
background = pygame.image.load("C:\\Users\\ryanp\\Documents\\GitHub\\nadocode-utilize1_game\\blue_background.png")
# 배경 이미지를 가져오는게 아니라 단순 색깔로 채우려는 경우라면 아래에서 screen.fill()을 사용해도 됨


running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    # screen.fill((0,0,255)) : (0,0,255) 색깔로 배경을 채우는 방법. 이 방법 사용 시, 배경 이미지를 불러오가 + 배경 그리기 과정이 필요 없음(게임화면 다시 그리기(pygame.display.update())는 필요함)
    screen.blit(background, (0,0)) # 배경 그리기: (좌측 상단 기준) 좌표 상 (0,0)부터 이미지 시작 
    pygame.display.update() # 게임화면을 다시 그리기!


pygame.quit()
