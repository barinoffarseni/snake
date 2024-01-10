import pygame
from random import randrange

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

def draw_apple(screen, apple_branch_color, light_reflection, branch, apple, light_reflection_color, apple_color, apple_styles):
    pygame.draw.circle(screen, apple_color, (apple[0] + apple_styles['x, y'][0], apple[1] + apple_styles['x, y'][1]), apple_styles['width'])
    pygame.draw.rect(screen, light_reflection_color, (apple[0] + light_reflection['light_reflection_1']['x, y'][0], apple[1] + light_reflection['light_reflection_1']['x, y'][1], light_reflection['light_reflection_1']['width'][0], light_reflection['light_reflection_1']['width'][1]))
    pygame.draw.rect(screen, light_reflection_color, (apple[0] + light_reflection['light_reflection_2']['x, y'][0], apple[1] + light_reflection['light_reflection_2']['x, y'][1], light_reflection['light_reflection_2']['width'][0], light_reflection['light_reflection_2']['width'][1]))
    pygame.draw.rect(screen, apple_branch_color, (apple[0] + branch['branch_start']['x, y'][0], apple[1] + branch['branch_start']['x, y'][1], branch['branch_start']['width'][0], branch['branch_start']['width'][1]))
    pygame.draw.rect(screen, apple_branch_color, (apple[0] + branch['branch_end']['x, y'][0], apple[1] + branch['branch_end']['x, y'][1], branch['branch_end']['width'][0], branch['branch_end']['width'][1]))

def get_new_apple_coordinates(snake, width, size):
    generate_again = True
    while generate_again:
        apple = randrange(0 ,width, size) , randrange(0 ,width, size)
        generate_again = False
        for part in snake:
            if part == apple:
                generate_again = True
                break
    return apple