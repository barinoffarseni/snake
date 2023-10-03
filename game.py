import pygame
from random import randrange

WINDOW_WIDTH = 800
SIZE = 50

TIMER = 5 


dx , dy = 0 , 0
x , y = randrange(0 ,WINDOW_WIDTH, SIZE) , randrange(0 ,WINDOW_WIDTH, SIZE)
apple = randrange(0 ,WINDOW_WIDTH, SIZE) , randrange(0 ,WINDOW_WIDTH, SIZE)
dirs = {"W":True, "D":True, "S":True, "A":True }
snake = [(x , y)]
lenght = 1

cut_tail = False

pygame.init()
screen = pygame.display.set_mode((1000, 800))
time = pygame.time.Clock()

while True:
    screen.fill(pygame.Color('black'))
    [(pygame.draw.rect(screen, pygame.Color('green'), (i, j, SIZE, SIZE))) for i, j in snake]
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, SIZE, SIZE))

    pygame.display.flip()
    time.tick(TIMER)

    x += dx * SIZE
    y += dy * SIZE
    
    if dx != 0 or dy != 0: 
        snake = [(x, y)] + snake
        
        if cut_tail == True: 
            snake.pop(-1)
        

    cut_tail = True

    if snake[0] == apple:
        apple = randrange(0 ,WINDOW_WIDTH, SIZE) , randrange(0 ,WINDOW_WIDTH, SIZE)

        cut_tail = False
    print(snake)

    if 0 > x or x > 950 or y < 0 or y > 750:
        exit()
    if len(snake) != len(set(snake)):
        exit()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    contr = pygame.key.get_pressed()
    if contr [pygame.K_w] and dirs ["W"]:
        dx , dy = 0 , -1
        dirs = {"W":True, "D":True, "S":False, "A":True }
    if contr [pygame.K_s] and dirs ["S"]:
        dx , dy = 0 , 1
        dirs = {"W":False, "D":True, "S":True, "A":True }
    if contr [pygame.K_a] and dirs ["A"]:
        dx , dy = -1 , 0
        dirs = {"W":True, "D":False, "S":True, "A":True }
    if contr [pygame.K_d] and dirs ["D"]:
        dx , dy = 1 , 0
        dirs = {"W":True, "D":True, "S":True, "A":False }