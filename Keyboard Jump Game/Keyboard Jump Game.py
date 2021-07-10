# 라이브러리
import pygame
import random
import time

# 게임 화면 구성
pygame.init()
WIDTH = 800
HEIGHT = 600
black = (0, 0, 0)
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Keyboard Jump Game')

# 이미지 크기 설정
background = pygame.image.load('keyback.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# 글꼴
font = pygame.font.Font('comic.ttf', 40)

# 함수 생성
word_speed = 0.5
score = 0


def new_word():
    global displayword, yourword, x_cor, y_cor, text, word_speed
    x_cor = random.randint(300, 700) # 랜덤으로 선택
    y_cor = 200 # 200높이에서 시작
    word_speed += 0.10 # 워드 칠 수록 내려오는 속도 증가
    yourword = '' # 공백에서 시작
    words = open("words.txt").read().split(', ') # words.txt 파일에서 단어 가져옴
    displayword = random.choice(words) # 내려오는 글자가 랜덤으로 선택
new_word()


font_name = pygame.font.match_font('comic.ttf')
def draw_text(display, text, size, x, y): # 주어진 글꼴과 크기로 텍스트 표시
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)


def game_front_screen(): # 게임 화면 및 게임 오버 화면 표시
    gameDisplay.blit(background, (0, 0))
    if not game_over:
        draw_text(gameDisplay, "GAME OVER!", 90, WIDTH / 2, HEIGHT / 4)
        draw_text(gameDisplay, "Score : " + str(score), 70, WIDTH / 2, HEIGHT / 2)
    else:
        draw_text(gameDisplay, "Press any key to begin!", 54, WIDTH / 2, 500)
    pygame.display.flip()

    waiting = True
    while waiting:

        for event in pygame.event.get(): # pygame 내 모든 이벤트 반환
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


game_over = True
game_start = True
while True:
    if game_over:
        if game_start:
            game_front_screen()
        game_start = False
    game_over = False

# 배경 구성
    background = pygame.image.load('teacher-background.jpg')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    character = pygame.image.load('char.jpg')
    character = pygame.transform.scale(character, (50, 50))
    wood = pygame.image.load('wood-.png')
    wood = pygame.transform.scale(wood, (90, 50))

    gameDisplay.blit(background, (0, 0))

    y_cor += word_speed
    gameDisplay.blit(wood, (x_cor-50, y_cor+15))
    gameDisplay.blit(character, (x_cor-100, y_cor))
    draw_text(gameDisplay, str(displayword), 40, x_cor, y_cor)
    draw_text(gameDisplay, 'Score:' + str(score), 40, WIDTH / 2, 5)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 틀릴 경우 게임 종료
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN: # 키보드 누르는대로 yourword에 입력
            yourword += pygame.key.name(event.key)

            if displayword.startswith(yourword): # 내가 친 글자와 제시된 글자가 같으면 스코어 +1점
                if displayword == yourword:
                    score += len(displayword)
                    new_word()
            else: # 틀릴 경우 2초 후 화면 꺼짐
                game_front_screen()
                time.sleep(2)
                pygame.quit()

    if y_cor < HEIGHT-5: # 글자가 화면 밑에 닿으면 게임오버
        pygame.display.update()
    else:
        game_front_screen()
