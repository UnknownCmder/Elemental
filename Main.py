import pygame
import sys

# 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 제목
pygame.display.set_caption("Pygame 기본 템플릿")

# FPS 설정
clock = pygame.time.Clock()

# 색상
WHITE = (255, 255, 255)

# 게임 루프
running = True
while running:
    # FPS 설정 (초당 60프레임)
    clock.tick(60)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 배경 그리기
    screen.fill(WHITE)

    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()
