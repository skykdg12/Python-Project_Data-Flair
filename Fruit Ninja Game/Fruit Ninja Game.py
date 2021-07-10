# import modules
import pygame
import sys
import os
import random

# 화면 생성
player_lives = 3
score = 0
fruits = ['melon', 'orange', 'pomegranate', 'guava', 'bomb']

# pygame 초기화 및 window 생성
WIDTH = 800
HEIGHT = 500
FPS = 12  # display 새로고침 주기 설정. 1/12초마다 새로 고침
pygame.init()
pygame.display.set_caption('FRUIT NINJA')  # caption
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))  # 화면 크기 설정
clock = pygame.time.Clock()

# 색 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


background = pygame.image.load('back.jpg')  # 게임 배경화면
font = pygame.font.Font(os.path.join(os.getcwd(), 'comic.ttf'), 32)
score_text = font.render('Score : ' + str(score), True, (255, 255, 255))  # score 표시
lives_icon = pygame.image.load('images/white_lives.png')

# 과일dict 구조
def generate_random_fruits(fruit):
    fruit_path = "images/" + fruit + ".png"
    data[fruit] = {
        'img': pygame.image.load(fruit_path),
        'x': random.randint(100, 500),  # 과일 위치
        'y': 800,
        'speed_x': random.randint(-10, 10),  # x 방향으로 과일의 속도 조정
        'speed_y': random.randint(-80, -60),  # y 방향 과일 속도 조정
        'throw': False,  # 과일이 만약 화면 범위 밖으로 사라지면 삭제시킴
        't': 0,
        'hit': False,
    }

    # 다음 랜덤한 과일을 [0,0, 1.0] 범위로 던짐, 게임디스플레이 안으로 넣기 위함
    if random.random() >= 0.75:
        data[fruit]['throw'] = True
    else:
        data[fruit]['throw'] = False


# 무작위 과일 데이터를 보관하는 dict
data = {}
for fruit in fruits:
    generate_random_fruits(fruit)

def hide_cross_lives(x, y):
    gameDisplay.blit(pygame.image.load("images/red_lives.png"), (x, y))


# generic method 스크린에 폰트를 넣기 위함
font_name = pygame.font.match_font('comic.ttf')


def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)  # blit은 이미지나 텍스르를 화면에 그림

# draw players lives
def draw_lives(display, x, y, lives, image):
    for i in range(lives):
        img = pygame.image.load(image)
        img_rect = img.get_rect()  # x자 아이콘을 오른쪽 상단에 놓음
        img_rect.x = int(x + 35 * i)  # 다음 x자 아이콘 설정
        img_rect.y = y  # x자 아이콘이 스크린에 몇개 있는지 표시
        display.blit(img, img_rect)

# 게임오버 화면 및 메인 화면
def show_gameover_screen():
    gameDisplay.blit(background, (0, 0))
    draw_text(gameDisplay, "FRUIT NINJA!", 90, WIDTH / 2, HEIGHT / 4)
    if not game_over:
        draw_text(gameDisplay, "Score : " + str(score),
                  50, WIDTH / 2, HEIGHT / 2)

    draw_text(gameDisplay, "Press a key to begin!",
              64, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

# game loop
first_round = True
game_over = True
game_running = True
while game_running:
    if game_over:
        if first_round:
            show_gameover_screen()
            first_round = False
        game_over = False
        player_lives = 3
        draw_lives(gameDisplay, 690, 5, player_lives, 'images/red_lives.png')
        score = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    gameDisplay.blit(background, (0, 0))
    gameDisplay.blit(score_text, (0, 0))
    draw_lives(gameDisplay, 690, 5, player_lives, 'images/red_lives.png')

    for key, value in data.items():
        if value['throw']:
            value['x'] += value['speed_x']  # x방향으로 과일 이동
            value['y'] += value['speed_y']  # y방향으로 과일 이동
            value['speed_y'] += (1 * value['t'])  # y-corrdinate 상승
            value['t'] += 1  # y방향 과일 속도 상승

            if value['y'] <= 880:
                # 과일을 스크린 안에서 동적으로 표시
                gameDisplay.blit(value['img'], (value['x'], value['y']))
            else:
                generate_random_fruits(key)

            current_position = pygame.mouse.get_pos()  # 마우스와 디스플레이에서의 커서를 일치시킴

            if not value['hit'] and current_position[0] > value['x'] and current_position[0] < value['x'] + 60 \
                and current_position[1] > value['y'] and current_position[1] < value['y'] + 60:
                if key == 'bomb':
                    player_lives -= 1
                    if player_lives == 0:
                        hide_cross_lives(690, 15)
                    elif player_lives == 1:
                        hide_cross_lives(725, 15)
                    elif player_lives == 2:
                        hide_cross_lives(760, 15)

                    # 폭탄을 3번 터트리면 게임오버 메세지와함께 게임화면 리셋
                    if player_lives < 0:
                        show_gameover_screen()
                        game_over = True

                    half_fruit_path = "images/explosion.png"
                else:
                    half_fruit_path = "images/" + "half_" + key + ".png"

                value['img'] = pygame.image.load(half_fruit_path)
                value['speed_x'] += 10
                if key != 'bomb':
                    score += 1
                score_text = font.render(
                    'Score : ' + str(score), True, (255, 255, 255))
                value['hit'] = True
        else:
            generate_random_fruits(key)
    pygame.display.update()
    clock.tick(FPS)  # loop를 일정한 속도로 조정

pygame.quit()
