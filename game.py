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

dx , dy = 0 , 0
x , y = randrange(0 ,WINDOW_WIDTH, SIZE) , randrange(0 ,WINDOW_WIDTH, SIZE)
snake = [(x , y)]
left_eyes_x, left_eyes_y = 10, 30
right_eyes_x, right_eyes_y = 30, 30

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 66, bold=True)
background_color = pygame.Color('black')
snake_color = pygame.Color('green')
apple_color = pygame.Color('red')
win_title_color = pygame.Color('yellow')
fail_title_color = pygame.Color('purple')
win_title_text = 'YOU WIN'
fail_title_text = 'GAME OVER'
eyes_colors = pygame.Color('white')
# eyes = pygame.draw.rect(snake, eyes_colors, 10, 10)
img = pygame.image.load('22.jpg')
img = pygame.transform.scale(img, (WINDOW_WIDTH, WINDOW_WIDTH)) 

pygame.mixer.init()
pygame.mixer.music.load('audio/birds.mp3')
pygame.mixer.music.play()

apple = get_new_apple_coordinates(snake)
game_status = 'play'

while True:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if game_status == 'win':
        screen.blit((font.render(win_title_text, 1, win_title_color)), (WINDOW_WIDTH // 2 - 200, WINDOW_WIDTH // 3))
        pygame.display.flip()
        pygame.mixer.music.load('audio/2.ogg')
        pygame.mixer.music.play()
        continue

    if game_status == 'fail':
        screen.blit((font.render(fail_title_text, 1, fail_title_color)), (WINDOW_WIDTH // 2 - 200, WINDOW_WIDTH // 3))
        pygame.display.flip()
        pygame.mixer.music.set_volume(0.5)
        continue

    audio_numbers = randrange(0, 3)
    screen.fill(background_color)
    screen.blit(img, (0, 0))
    [(pygame.draw.rect(screen, snake_color, (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
    (pygame.draw.rect(screen, eyes_colors,(snake[0][0] + left_eyes_x, snake[0][1] + left_eyes_y, 10, 10)))
    (pygame.draw.rect(screen, eyes_colors,(snake[0][0] + right_eyes_x, snake[0][1] + right_eyes_y, 10, 10)))
    pygame.draw.rect(screen, apple_color, (*apple, SIZE, SIZE))
    pygame.display.flip()

    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.play()

    x += dx * SIZE
    y += dy * SIZE
    next_cell = (x, y)

    if dx != 0 or dy != 0:
        snake = [next_cell] + snake 
        if next_cell == apple:
            if len(snake) == int(WINDOW_WIDTH / SIZE * WINDOW_WIDTH / SIZE):
                game_status = 'win'
                continue

            apple = get_new_apple_coordinates(snake)
            pygame.mixer.Sound('audio/' + str(audio_numbers) + '.ogg').play()
        else:
            snake.pop(-1)

    if 0 > x or x > WINDOW_WIDTH - SIZE or y < 0 or y > WINDOW_WIDTH - SIZE or len(snake) != len(set(snake)):
        game_status = 'fail'
        continue

    odx, ody = dx, dy
    contr = pygame.key.get_pressed()
    if contr [pygame.K_w] and ody != 1:
        dx , dy = 0 , -1
        left_eyes_x, left_eyes_y = 10, 10
        right_eyes_x, right_eyes_y = 30, 10
    if contr [pygame.K_s] and ody != -1:
        dx , dy = 0 , 1
        left_eyes_x, left_eyes_y = 10, 30
        right_eyes_x, right_eyes_y = 30, 30
    if contr [pygame.K_a] and odx != 1:
        dx , dy = -1 , 0
        left_eyes_x, left_eyes_y = 10, 10
        right_eyes_x, right_eyes_y = 10, 30
    if contr [pygame.K_d] and odx != -1:
        dx , dy = 1 , 0
        left_eyes_x, left_eyes_y = 30, 10
        right_eyes_x, right_eyes_y = 30, 30