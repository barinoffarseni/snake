import pygame 
from random import randrange
from snake_styles import get_tail_styles, get_head_offset, draw_eyes, get_eyes_offset
from snake_styles import snake_color, eyes_colors, pupil_width, eyes_width

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

apple_styles = {
    'width': (22),
    'x, y': (25, 25)
}

light_reflection = {
    'light_reflection_1': {
        'x, y': (40, 10),
        'width': (5, 10),
    },
    'light_reflection_2': {
        'x, y': (35, 10),
        'width': (5, 5),
    },
}

branch = {
    'branch_start': {
        'x, y': (20, 5),
        'width': (10, 10),
    },
    'branch_end': {
        'x, y': [15, 0],
        'width': (10, 10),
    },
}

dx , dy = 0 , 0
x , y = randrange(0 ,WINDOW_WIDTH, SIZE) , randrange(0 ,WINDOW_WIDTH, SIZE)
snake = [(x , y)]

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 66, bold=True)
background_color = pygame.Color('black')
apple_color = pygame.Color('red')
win_title_color = pygame.Color('yellow')
fail_title_color = pygame.Color('purple')
apple_branch_color = pygame.Color('brown')
light_reflection_color = pygame.Color('white')
win_title_text = 'YOU WIN'
fail_title_text = 'GAME OVER'

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
    def chess_field():
        for i in range(0, WINDOW_WIDTH, SIZE):
            for j in range(0, WINDOW_WIDTH, SIZE):
                if i == 0 and j % 100 == 0:
                    pygame.draw.rect(screen, light_reflection_color, (i, j, SIZE, SIZE))
                if j == 50 and i == 50:
                    pygame.draw.rect(screen, light_reflection_color, (i, j, SIZE, SIZE))
                if j % 100 == 0 and i % 100 == 0:
                    pygame.draw.rect(screen, light_reflection_color, (i, j, SIZE, SIZE))
                if j % 100 == 50 and i % 100 == 50:
                    pygame.draw.rect(screen, light_reflection_color, (i, j, SIZE, SIZE))

    chess_field()

    for cell in snake:
        if cell != snake[0] and cell != snake[len(snake)-1]:
            pygame.draw.rect(screen, snake_color, (cell[0], cell[1], SIZE, SIZE))
        else:
            pygame.draw.circle(screen, snake_color, (cell[0] + SIZE / 2, cell[1] + SIZE / 2), int(SIZE / 2), int(SIZE / 2))
            if len(snake) > 1:
                head = get_head_offset(dx, dy, snake)
                tail_styles = get_tail_styles(snake)
                pygame.draw.rect(screen, snake_color, (snake[len(snake)-1][0] + tail_styles['x_y'][0], snake[len(snake)-1][1] + tail_styles['x_y'][1], tail_styles['width_tail_x_y'][0], tail_styles['width_tail_x_y'][1]))
                pygame.draw.rect(screen, snake_color, (snake[0][0] + head['x_y'][0], snake[0][1] + head['x_y'][1], head['width_head_x_y'][0], head['width_head_x_y'][1]))
    eyes = get_eyes_offset(dy, dx)
    draw_eyes(eyes, screen, eyes_colors, background_color, snake, eyes_width, pupil_width)
    pygame.draw.circle(screen, apple_color, (apple[0] + apple_styles['x, y'][0], apple[1] + apple_styles['x, y'][1]), apple_styles['width'])
    pygame.draw.rect(screen, light_reflection_color, (apple[0] + light_reflection['light_reflection_1']['x, y'][0], apple[1] + light_reflection['light_reflection_1']['x, y'][1], light_reflection['light_reflection_1']['width'][0], light_reflection['light_reflection_1']['width'][1]))
    pygame.draw.rect(screen, light_reflection_color, (apple[0] + light_reflection['light_reflection_2']['x, y'][0], apple[1] + light_reflection['light_reflection_2']['x, y'][1], light_reflection['light_reflection_2']['width'][0], light_reflection['light_reflection_2']['width'][1]))
    pygame.draw.rect(screen, apple_branch_color, (apple[0] + branch['branch_start']['x, y'][0], apple[1] + branch['branch_start']['x, y'][1], branch['branch_start']['width'][0], branch['branch_start']['width'][1]))
    pygame.draw.rect(screen, apple_branch_color, (apple[0] + branch['branch_end']['x, y'][0], apple[1] + branch['branch_end']['x, y'][1], branch['branch_end']['width'][0], branch['branch_end']['width'][1]))
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
            
            branch['branch_end']['x, y'][0] = randrange(15, 30, 5)
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
    if contr [pygame.K_s] and ody != -1:
        dx , dy = 0 , 1
    if contr [pygame.K_a] and odx != 1:
        dx , dy = -1 , 0
    if contr [pygame.K_d] and odx != -1:
        dx , dy = 1 , 0