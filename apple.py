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
        'x, y': (25, 25)
    }
    self.light_reflection_color = pygame.Color('white')
    self.light_reflection = {
        'light_reflection_1': {
            'x, y': (40, 10),
            'width': (5, 10),
        },
        'light_reflection_2': {
            'x, y': (35, 10),
            'width': (5, 5),
        }
    }

    self.branch = {
        'branch_start': {
            'x, y': (20, 5),
            'width': (10, 10),
        },
        'branch_end': {
            'x, y': [15, 0],
            'width': (10, 10),
        },
    }
  
  def draw(self,screen):
    pygame.draw.circle(screen, self.color, (self.coordinates[0] + self.styles['x, y'][0], self.coordinates[1] + self.styles['x, y'][1]), self.styles['width'])
    pygame.draw.rect(screen, self.light_reflection_color, (self.coordinates[0] + self.light_reflection['light_reflection_1']['x, y'][0], self.coordinates[1] + self.light_reflection['light_reflection_1']['x, y'][1], self.light_reflection['light_reflection_1']['width'][0], self.light_reflection['light_reflection_1']['width'][1]))
    pygame.draw.rect(screen, self.light_reflection_color, (self.coordinates[0] + self.light_reflection['light_reflection_2']['x, y'][0], self.coordinates[1] + self.light_reflection['light_reflection_2']['x, y'][1], self.light_reflection['light_reflection_2']['width'][0], self.light_reflection['light_reflection_2']['width'][1]))
    pygame.draw.rect(screen, self.branch_color, (self.coordinates[0] + self.branch['branch_start']['x, y'][0], self.coordinates[1] + self.branch['branch_start']['x, y'][1], self.branch['branch_start']['width'][0], self.branch['branch_start']['width'][1]))
    pygame.draw.rect(screen, self.branch_color, (self.coordinates[0] + self.branch['branch_end']['x, y'][0], self.coordinates[1] + self.branch['branch_end']['x, y'][1], self.branch['branch_end']['width'][0], self.branch['branch_end']['width'][1]))

  def randomize_branch(self):
    self.branch['branch_end']['x, y'][0] = randrange(15, 30, 5)

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