import pygame

class Apple:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.color = pygame.Color('red')
    self.branch_color = pygame.Color('brown')
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

  def get_coordinates(self):
    return (self.x, self.y)
  
  def draw(self):
    self.draw_apple(screen, self.branch_color, self.light_reflection, self.branch, self.get_coordinates(), self.light_reflection_color, self.color, self.styles)

  def draw_apple(screen, apple_branch_color, light_reflection, branch, apple, light_reflection_color, apple_color, apple_styles):
    pygame.draw.circle(screen, apple_color, (apple[0] + apple_styles['x, y'][0], apple[1] + apple_styles['x, y'][1]), apple_styles['width'])
    pygame.draw.rect(screen, light_reflection_color, (apple[0] + light_reflection['light_reflection_1']['x, y'][0], apple[1] + light_reflection['light_reflection_1']['x, y'][1], light_reflection['light_reflection_1']['width'][0], light_reflection['light_reflection_1']['width'][1]))
    pygame.draw.rect(screen, light_reflection_color, (apple[0] + light_reflection['light_reflection_2']['x, y'][0], apple[1] + light_reflection['light_reflection_2']['x, y'][1], light_reflection['light_reflection_2']['width'][0], light_reflection['light_reflection_2']['width'][1]))
    pygame.draw.rect(screen, apple_branch_color, (apple[0] + branch['branch_start']['x, y'][0], apple[1] + branch['branch_start']['x, y'][1], branch['branch_start']['width'][0], branch['branch_start']['width'][1]))
    pygame.draw.rect(screen, apple_branch_color, (apple[0] + branch['branch_end']['x, y'][0], apple[1] + branch['branch_end']['x, y'][1], branch['branch_end']['width'][0], branch['branch_end']['width'][1]))
