import pygame
from random import randrange

class Snake:
    def __init__(self, width, size):
        self.x = randrange(0, width, size)
        self.y = randrange(0, width, size)
        self.segments = [(self.x , self.y)]

        self.dx = 0
        self.dy = 0

        self.eyes_colors = pygame.Color('white')
        self.snake_color = pygame.Color('green')
    
    def draw(self, screen, SIZE):
        for cell in self.segments:
            if cell != self.segments[0] and cell != self.segments[len(self.segments)-1]:
                pygame.draw.rect(screen, self.snake_color, (cell[0], cell[1], SIZE, SIZE))
            else:
                pygame.draw.circle(screen, self.snake_color, (cell[0] + SIZE / 2, cell[1] + SIZE / 2), int(SIZE / 2), int(SIZE / 2))
                if len(self.segments) > 1:
                    self.head = self.get_head_offset(self.dx, self.dy)
                    self.tail_styles = self.get_tail_styles()
                    pygame.draw.rect(screen, self.snake_color, (self.segments[len(self.segments)-1][0] + self.tail_styles['x'], self.segments[len(self.segments)-1][1] + self.tail_styles['y'], self.tail_styles['width_tail_x_y'][0], self.tail_styles['width_tail_x_y'][1]))
                    pygame.draw.rect(screen, self.snake_color, (self.segments[0][0] + self.head['x'], self.segments[0][1] + self.head['y'], self.head['width_head_x_y'][0], self.head['width_head_x_y'][1]))
        
    def get_tail_styles(self):
        tail = self.segments[len(self.segments)-1]
        body = self.segments[len(self.segments)-2]
        dx = tail[0] - body[0]
        dy = tail[1] - body[1]
        if dx < 0:
            self.tail_styles = {
                'x': (25),
                'y': (0),
                'width_tail_x_y': (25, 50)
            }
        if dx > 0:
            self.tail_styles = {
                'x': (0),
                'y': (0),
                'width_tail_x_y': (25, 50)
            }
        if dy < 0:
            self.tail_styles = {
                'x': (0),
                'y': (25),
                'width_tail_x_y': (50, 25)
            }
        if dy > 0:
            self.tail_styles = {
                'x': (0),
                'y': (0),
                'width_tail_x_y': (50, 25)
            }
        return self.tail_styles 

    def get_head_offset(self, dx, dy):
        self.head = self.segments[0]
        self.body = self.segments[1]
        odx = self.head[0] - self.body[0]
        ody = self.head[1] - self.body[1]
        if ody < 0:
            ody = -1
        if ody > 0:
            ody = 1
        if odx < 0:
            odx = -1
        if odx > 0:
            odx = 1
        if dx == odx and dy == ody and dy == -1:
            self.head = {
                'x': (0),
                'y': (25),
                'width_head_x_y': (50, 25)
            }
        if dx == odx and dy == ody and dy == 1:
            self.head ={
                'x': (0),
                'y': (0),
                'width_head_x_y': (50, 25)
            }
        if dx == odx and dy == ody and dx == -1:
            self.head = {
                'x': (25),
                'y': (0),
                'width_head_x_y': (25, 50)
            }
        if dx == odx and dy == ody and dx == 1:
            self.head = {
                'x': (0),
                'y': (0),
                'width_head_x_y': (25, 50)
            }
        if dx != odx and dy != ody and (odx > 0 and dy < 0) or (odx > 0 and dy > 0):
            self.head = {
                'x': (0),
                'y': (0),
                'width_head_x_y': (25, 50)
            }
        if dx != odx and dy != ody and (odx < 0 and dy > 0) or (odx < 0 and dy < 0):
            self.head = {
                'x': (25),
                'y': (0),
                'width_head_x_y': (25, 50)
            }
        if dx != odx and dy != ody and (ody > 0 and dx < 0) or (ody > 0 and dx > 0):
            self.head = {
                'x': (0),
                'y': (0),
                'width_head_x_y': (50, 25)
            }
        if dx != odx and dy != ody and (ody < 0 and dx > 0) or (ody < 0 and dx < 0):
            self.head = {
                'x': (0),
                'y': (25),
                'width_head_x_y': (50, 25)
            }
        return self.head

    def draw_eyes(self, screen, background_color):
        eyes = self.get_eyes_offset()
        pygame.draw.rect(screen, self.eyes_colors,(self.segments[0][0] + eyes['left_eye']['x'], self.segments[0][1] + eyes['left_eye']['y'], eyes['left_eye']['eyes_width'][0], eyes['left_eye']['eyes_width'][1]))
        pygame.draw.rect(screen, self.eyes_colors,(self.segments[0][0] + eyes['right_eye']['x'], self.segments[0][1] + eyes['right_eye']['y'], eyes['right_eye']['eyes_width'][0], eyes['right_eye']['eyes_width'][1]))
        pygame.draw.rect(screen, background_color,(self.segments[0][0] + eyes['left_eye']['pupil_x'], self.segments[0][1] + eyes['left_eye']['pupil_y'], eyes['left_eye']['pupil_width'][0], eyes['left_eye']['pupil_width'][1]))
        pygame.draw.rect(screen, background_color,(self.segments[0][0] + eyes['right_eye']['pupil_x'], self.segments[0][1] + eyes['right_eye']['pupil_y'], eyes['right_eye']['pupil_width'][0], eyes['right_eye']['pupil_width'][0]))

    def get_eyes_offset(self):
        self.eyes = {
            'left_eye': {
                'x': (10),
                'y': (30),
                'eyes_width': (10, 10),
                'pupil_x': (15),
                'pupil_y': (35),
                'pupil_width': (5, 5)
            },
            'right_eye': {
                'x': (30),
                'y': (30),
                'eyes_width': (10, 10),
                'pupil_x': (35),
                'pupil_y': (35),
                'pupil_width': (5, 5) 
            }
        }

        if self.dx == -1:
            self.eyes = {
                # влево
                'left_eye': {
                    'x': (10),
                    'y': (10),
                    'eyes_width': (10, 10),
                    'pupil_x': (15),
                    'pupil_y': (15),
                    'pupil_width': (5, 5) 
                },
                'right_eye': {
                    'x': (10),
                    'y': (30),
                    'eyes_width': (10, 10),
                    'pupil_x': (15),
                    'pupil_y': (35),
                    'pupil_width': (5, 5)  
                }
            }

        if self.dx == 1:
            self.eyes = {
            # в право 
                'left_eye': {
                    'x': (30),
                    'y': (10),
                    'eyes_width': (10, 10),
                    'pupil_x': (35),
                    'pupil_y': (15),
                    'pupil_width': (5, 5) 
                },
                'right_eye': {
                    'x': (30),
                    'y': (30),
                    'eyes_width': (10, 10),
                    'pupil_x': (35),
                    'pupil_y': (35),
                    'pupil_width': (5, 5)
                }
            }

        if self.dy == -1:
            self.eyes = {
                # 'eyes_width': (10, 10),
                # вверх
                'left_eye': {
                    'x': (10),
                    'y': (10),
                    'eyes_width': (10, 10),
                    'pupil_x': (15),
                    'pupil_y': (10),
                    'pupil_width': (5, 5)
                },
                'right_eye': {
                    'x': (30),
                    'y': (10),
                    'eyes_width': (10, 10),
                    'pupil_x': (35),
                    'pupil_y': (10),
                    'pupil_width': (5, 5) 
                }
            }

        if self.dy == 1:
            self.eyes = {
                # вниз
                'left_eye': {
                    'x': (10),
                    'y': (30),
                    'eyes_width': (10, 10),
                    'pupil_x': (15),
                    'pupil_y': (35),
                    'pupil_width': (5, 5)
                },
                'right_eye': {
                    'x': (30),
                    'y': (30),
                    'eyes_width': (10, 10),
                    'pupil_x': (35),
                    'pupil_y': (35),
                    'pupil_width': (5, 5) 
                }
            }
                
        return self.eyes