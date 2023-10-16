import pygame
from random import randrange

WINDOW_WIDTH = 200
SIZE = 50

TIMER = 5 


dx , dy = 0 , 0
x , y = randrange(0 ,WINDOW_WIDTH, SIZE) , randrange(0 ,WINDOW_WIDTH, SIZE)
apple = randrange(0 ,WINDOW_WIDTH, SIZE) , randrange(0 ,WINDOW_WIDTH, SIZE)
snake = [(x , y)]

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
time = pygame.time.Clock()

generate_again =True
while generate_again:
    apple = randrange(0 ,WINDOW_WIDTH, SIZE) , randrange(0 ,WINDOW_WIDTH, SIZE)
    generate_again = False
    for part in snake:
        if part == apple:
            generate_again = True
            break
        
while True:
    screen.fill(pygame.Color('black'))
    [(pygame.draw.rect(screen, pygame.Color('green'), (i, j, SIZE, SIZE))) for i, j in snake]
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, SIZE, SIZE))

    pygame.display.flip()
    time.tick(TIMER)

    x += dx * SIZE
    y += dy * SIZE
    next_cell = (x, y)
    
    if dx != 0 or dy != 0:
        snake = [next_cell] + snake 
        if next_cell == apple:
            generate_again =True
            while generate_again:
                apple = randrange(0 ,WINDOW_WIDTH, SIZE) , randrange(0 ,WINDOW_WIDTH, SIZE)
                generate_again = False
                for part in snake:
                    if part == apple:
                        generate_again = True
                        break
        else:
            snake.pop(-1)

    if 0 > x or x > WINDOW_WIDTH - SIZE or y < 0 or y > WINDOW_WIDTH - SIZE:
        exit()
    if len(snake) != len(set(snake)):
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

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