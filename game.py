import pygame
from random import randrange

WINDOW_WIDTH = 800
SIZE = 50
FPS = 5

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
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 66, bold=True)
background_color = pygame.Color('black')
snake_color = pygame.Color('green')
apple_color = pygame.Color('red')

pygame.mixer.init()
# pygame.mixer.pre_init(44100, -16, 1, 512) # нужно узнать что это такое
pygame.mixer.music.load('audio/birds.mp3')
pygame.mixer.music.play()

apple = get_new_apple_coordinates(snake)
# game_status = 'play'

while True:
    # if game_status == 'play'
    audio_numbers = randrange(0, 3)
    screen.fill(background_color)
    [(pygame.draw.rect(screen, snake_color, (i, j, SIZE, SIZE))) for i, j in snake]
    pygame.draw.rect(screen, apple_color, (*apple, SIZE, SIZE))
    pygame.display.flip()
    clock.tick(FPS)

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
                    screen.blit((font.render('YOU WIN', 1, pygame.Color('yellow'))), (WINDOW_WIDTH // 2 - 200, WINDOW_WIDTH // 3))
                    pygame.display.flip()
                    pygame.mixer.music.load('audio/2.ogg')
                    pygame.mixer.music.play()
                    pressing_the_cross()

            apple = get_new_apple_coordinates(snake)
            pygame.mixer.Sound('audio/' + str(audio_numbers) + '.ogg').play()
        else:
            snake.pop(-1)

    if 0 > x or x > WINDOW_WIDTH - SIZE or y < 0 or y > WINDOW_WIDTH - SIZE or len(snake) != len(set(snake)):
        while True:
            screen.blit((font.render('GAME OVER', 1, pygame.Color('purple'))), (WINDOW_WIDTH // 2 - 200, WINDOW_WIDTH // 3))
            pygame.display.flip()
            pygame.mixer.music.set_volume(0.5)
            pressing_the_cross()
    pressing_the_cross()

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