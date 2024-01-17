import pygame
import apple
import snake 
from random import randrange

WINDOW_WIDTH = 800
SIZE = 50
FPS = 5

x , y = randrange(0 ,WINDOW_WIDTH, SIZE) , randrange(0 ,WINDOW_WIDTH, SIZE)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 66, bold=True)
background_color = pygame.Color('black')
background_color_2 = pygame.Color('white')
win_title_color = pygame.Color('yellow')
fail_title_color = pygame.Color('purple')
win_title_text = 'YOU WIN'
fail_title_text = 'GAME OVER'

pygame.mixer.init()
pygame.mixer.music.load('audio/birds.mp3')
pygame.mixer.music.play()

game_status = 'play'

def get_new_apple_coordinates(snake, width, size):
    generate_again = True
    while generate_again:
        apple = randrange(0 ,width, size), randrange(0 ,width, size)
        generate_again = False
        for part in snake:
            if part == apple:
                generate_again = True
                break
    return apple

snake = snake.Snake(x, y)
print(snake.segments)
apple_x, apple_y = get_new_apple_coordinates(snake.segments, WINDOW_WIDTH, SIZE)
apple = apple.Apple(apple_x, apple_y)

game_status = 'play'

def win_state():
    screen.blit((font.render(win_title_text, 1, win_title_color)), (WINDOW_WIDTH // 2 - 200, WINDOW_WIDTH // 3))
    pygame.display.flip()
    pygame.mixer.music.load('audio/2.ogg')
    pygame.mixer.music.play()

def lose_state():
    screen.blit((font.render(fail_title_text, 1, fail_title_color)), (WINDOW_WIDTH // 2 - 200, WINDOW_WIDTH // 3))
    pygame.display.flip()
    pygame.mixer.music.set_volume(0.5)

def draw_background():
    screen.fill(background_color)
    for i in range(0, WINDOW_WIDTH, SIZE):
        for j in range(0, WINDOW_WIDTH, SIZE):
            if i == 0 and j % 100 == 0:
                pygame.draw.rect(screen, background_color_2, (i, j, SIZE, SIZE))
            if j == 50 and i == 50:
                pygame.draw.rect(screen, background_color_2, (i, j, SIZE, SIZE))
            if j % 100 == 0 and i % 100 == 0:
                pygame.draw.rect(screen, background_color_2, (i, j, SIZE, SIZE))
            if j % 100 == 50 and i % 100 == 50:
                pygame.draw.rect(screen, background_color_2, (i, j, SIZE, SIZE))

def restart_music():
    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.play()

def play_eat_apple_sound():
    pygame.mixer.Sound('audio/' + str(randrange(0, 3)) + '.ogg').play()
dx, dy = 0, 0
def control(dx, dy):
    odx, ody = dx, dy
    contr = pygame.key.get_pressed()
    if contr [pygame.K_w] and ody != 1:
        return 0, -1
    if contr [pygame.K_s] and ody != -1:
        return 0, 1
    if contr [pygame.K_a] and odx != 1:
        return -1, 0
    if contr [pygame.K_d] and odx != -1:
        return 1, 0

    return dx, dy

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if game_status == 'win':
        win_state()
        continue

    if game_status == 'fail':
        lose_state()
        continue

    draw_background()
    # snake.draw()
    snake.draw(snake.snake_color, screen, SIZE)

    # snake.draw()
    eyes = snake.get_eyes_offset(snake.dy, snake.dx)

    # snake.draw()
    snake.draw_eyes(eyes, screen, snake.eyes_colors, background_color, snake.eyes_width, snake.pupil_width)

    apple.draw(screen)

    pygame.display.flip()

    restart_music()

    x += snake.dx * SIZE
    y += snake.dy * SIZE

    next_cell = (x, y)
    if snake.dx != 0 or snake.dy != 0:
        snake = [next_cell] + snake 
        if next_cell == apple.get_coordinates():
            if len(snake) == int(WINDOW_WIDTH / SIZE * WINDOW_WIDTH / SIZE):
                game_status = 'win'
                continue

            apple.randomize_branch()
            apple.x, apple.y = get_new_apple_coordinates(snake, WINDOW_WIDTH, SIZE)

            play_eat_apple_sound()
        else:
            snake.segments.pop(-1)

    if 0 > x or x > WINDOW_WIDTH - SIZE or y < 0 or y > WINDOW_WIDTH - SIZE or len(snake.segments) != len(set(snake.segments)):
        game_status = 'fail'
        continue

    dx , dy = control(dx, dy)