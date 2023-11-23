import pygame
from random import randrange

WINDOW_WIDTH = 800
SIZE = 50
TIMER = 5 

def get_new_apple_coordinates(snake):
    generate_again = True
    while generate_again:
        apple = randrange(0 ,WINDOW_WIDTH, SIZE) , randrange(0 ,WINDOW_WIDTH, SIZE)
        generate_again = False
        for part in snake:
            if part == apple:
                generate_again = True
                break
    return apple 

def pressing_the_cross():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

dx , dy = 0 , 0
x , y = randrange(0 ,WINDOW_WIDTH, SIZE) , randrange(0 ,WINDOW_WIDTH, SIZE)
snake = [(x , y)]

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))

pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 1, 512)

time = pygame.time.Clock()
pygame.mixer.music.load('audio/birds.mp3')
pygame.mixer.music.play()
font_end = pygame.font.SysFont('arial', 66, bold=True)

apple = get_new_apple_coordinates(snake)
while True:
    audio_nambers = randrange(0, 3)
    screen.fill(pygame.Color('black'))
    [(pygame.draw.rect(screen, pygame.Color('green'), (i, j, SIZE, SIZE))) for i, j in snake]
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, SIZE, SIZE))
    pygame.display.flip()
    time.tick(TIMER)

    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.play()
    x += dx * SIZE
    y += dy * SIZE
    next_cell = (x, y)

    if dx != 0 or dy != 0:
        snake = [next_cell] + snake 
        if next_cell == apple:
                if len(snake) == int(WINDOW_WIDTH / SIZE * WINDOW_WIDTH / SIZE):
                    while True:
                        screen.blit((font_end.render('YOU WIN', 1, pygame.Color('yellow'))), (WINDOW_WIDTH // 2 - 200, WINDOW_WIDTH // 3))
                        pygame.display.flip()
                        pygame.mixer.music.load('audio/2.ogg')
                        pygame.mixer.music.play()
                        close_game()

                apple = get_new_apple_coordinates(snake)
                pygame.mixer.Sound('audio/' + str(audio_nambers) + '.ogg').play()
        else:
            snake.pop(-1)

    if 0 > x or x > WINDOW_WIDTH - SIZE or y < 0 or y > WINDOW_WIDTH - SIZE or len(snake) != len(set(snake)):
        while True:
            screen.blit((font_end.render('GAME OVER', 1, pygame.Color('purple'))), (WINDOW_WIDTH // 2 - 200, WINDOW_WIDTH // 3))
            pygame.display.flip()
            pygame.mixer.music.set_volume(0.5)
            close_game()
    close_game()

    odx, ody = dx, dy
    contr = pygame.key.get_pressed()
    if contr [pygame.K_w] and ody != 1:
        dx , dy = 0 , -1
    if contr [pygame.K_s] and ody != -1:
        dx , dy = 0 , 1
    if contr [pygame.K_a] and odx != 1:
        dx , dy = -1 , 0
    if contr [pygame.K_d] and odx != -1:
        dx , dy = 1 , 0