import pygame
from random import randrange

class Apple:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.color = pygame.Color('red')
    self.branch_color = pygame.Color('brown')
    self.coordinates = (self.x, self.y)
    self.styles = {
        'width': (22),
        'x': (25),
        'y': (25),
    }
    self.light_reflection_color = pygame.Color('white')
    self.light_reflection = {
        'light_reflection_1': {
            'x': (40),
            'y': (10),
            'width': (5, 10),
        },
        'light_reflection_2': {
            'x': (35),
            'y': (10),
            'width': (5, 5),
        }
    }

    self.branch = {
        'branch_start': {
            'x': (20),
            'y': (5),
            'width': (10, 10),
        },
        'branch_end': {
            'x': (15),
            'y': (0),
            'width': (10, 10),
        },
    }
  
  def draw(self,screen):
    pygame.draw.circle(screen, self.color, (self.coordinates[0] + self.styles['x'], self.coordinates[1] + self.styles['y']), self.styles['width'])
    pygame.draw.rect(screen, self.light_reflection_color, (self.coordinates[0] + self.light_reflection['light_reflection_1']['x'], self.coordinates[1] + self.light_reflection['light_reflection_1']['y'], self.light_reflection['light_reflection_1']['width'][0], self.light_reflection['light_reflection_1']['width'][1]))
    pygame.draw.rect(screen, self.light_reflection_color, (self.coordinates[0] + self.light_reflection['light_reflection_2']['x'], self.coordinates[1] + self.light_reflection['light_reflection_2']['y'], self.light_reflection['light_reflection_2']['width'][0], self.light_reflection['light_reflection_2']['width'][1]))
    pygame.draw.rect(screen, self.branch_color, (self.coordinates[0] + self.branch['branch_start']['x'], self.coordinates[1] + self.branch['branch_start']['y'], self.branch['branch_start']['width'][0], self.branch['branch_start']['width'][1]))
    pygame.draw.rect(screen, self.branch_color, (self.coordinates[0] + self.branch['branch_end']['x'], self.coordinates[1] + self.branch['branch_end']['y'], self.branch['branch_end']['width'][0], self.branch['branch_end']['width'][1]))

  def randomize_branch(self):
    self.branch['branch_end']['x'] = randrange(15, 30, 5)

  def get_new_apple_coordinates(self, snake, width, size):
    generate_again = True
    while generate_again:
        self.coordinates = randrange(0 ,width, size), randrange(0 ,width, size)
        generate_again = False
        for part in snake:
            if part == self.coordinates:
                generate_again = True
                break
    return self.coordinates