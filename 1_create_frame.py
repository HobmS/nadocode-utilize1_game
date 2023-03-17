import pygame

pygame.init() # 초기화 (pygame 사용 시 필수)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("HobmS") # 게임 이름 설정

# 실행 시, 게임이 실행되지만 진행할 것이 없어서 바로 종료됨
# 이벤트 루프: 사용자의 동작을 검사하는 것 -> 실행되어야 게임이 종료되지 않음
running = True
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가? (pygame에서 꼭 필요한 문장)
        if event.type == pygame.QUIT: # 창 닫기 버튼을 눌렀는가?
            running = False


# pygame 종료
pygame.quit()