import pygame

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.segments = [(self.x , self.y)]

        self.dx = 0
        self.dy = 0

        self.eyes_width = 10
        self.pupil_width = 5

        self.eyes_colors = pygame.Color('white')
        self.snake_color = pygame.Color('green')

    def draw(self, snake_color, screen, SIZE):
        self.draw_snake(snake_color, screen, SIZE)
    
    def draw_snake(self, snake_color, screen, SIZE):
        for cell in self.segments:
            if cell != self.segments[0] and cell != self.segments[len(self.segments)-1]:
                pygame.draw.rect(screen, snake_color, (cell[0], cell[1], SIZE, SIZE))
            else:
                pygame.draw.circle(screen, snake_color, (cell[0] + SIZE / 2, cell[1] + SIZE / 2), int(SIZE / 2), int(SIZE / 2))
                if len(self.segments) > 1:
                    head = self.get_head_offset(self.dx, self.dy)
                    tail_styles = self.get_tail_styles()
                    pygame.draw.rect(screen, snake_color, (self.segments[len(self.segments)-1][0] + tail_styles['x_y'][0], self.segments[len(self.segments)-1][1] + tail_styles['x_y'][1], tail_styles['width_tail_x_y'][0], tail_styles['width_tail_x_y'][1]))
                    pygame.draw.rect(screen, snake_color, (self.segments[0][0] + head['x_y'][0], self.segments[0][1] + head['x_y'][1], head['width_head_x_y'][0], head['width_head_x_y'][1]))
        
    def get_tail_styles(self):
        tail = self.segments[len(self.segments)-1]
        body = self.segments[len(self.segments)-2]
        dx = tail[0] - body[0]
        dy = tail[1] - body[1]
        if dx < 0:
            self.tail_styles = {
                'x_y': (25, 0),
                'width_tail_x_y': (25, 50)
            }
        if dx > 0:
            self.tail_styles = {
                'x_y': (0, 0),
                'width_tail_x_y': (25, 50)
            }
        if dy < 0:
            self.tail_styles = {
                'x_y': (0, 25),
                'width_tail_x_y': (50, 25)
            }
        if dy > 0:
            self.tail_styles = {
                'x_y': (0, 0),
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
                'x_y': (0, 25),
                'width_head_x_y': (50, 25)
            }
        if dx == odx and dy == ody and dy == 1:
            self.head ={
                'x_y': (0, 0),
                'width_head_x_y': (50, 25)
            }
        if dx == odx and dy == ody and dx == -1:
            self.head = {
                'x_y': (25, 0),
                'width_head_x_y': (25, 50)
            }
        if dx == odx and dy == ody and dx == 1:
            self.head = {
                'x_y': (0, 0),
                'width_head_x_y': (25, 50)
            }
        if dx != odx and dy != ody and (odx > 0 and dy < 0) or (odx > 0 and dy > 0):
            self.head = {
                'x_y': (0, 0),
                'width_head_x_y': (25, 50)
            }
        if dx != odx and dy != ody and (odx < 0 and dy > 0) or (odx < 0 and dy < 0):
            self.head = {
                'x_y': (25, 0),
                'width_head_x_y': (25, 50)
            }
        if dx != odx and dy != ody and (ody > 0 and dx < 0) or (ody > 0 and dx > 0):
            self.head = {
                'x_y': (0, 0),
                'width_head_x_y': (50, 25)
            }
        if dx != odx and dy != ody and (ody < 0 and dx > 0) or (ody < 0 and dx < 0):
            self.head = {
                'x_y': (0, 25),
                'width_head_x_y': (50, 25)
            }
        return self.head

    def draw_eyes(self, eyes, screen, eyes_colors, background_color, eyes_width, pupil_width):
        pygame.draw.rect(screen, eyes_colors,(self.segments[0][0] + eyes['left_eye']['x, y'][0], self.segments[0][1] + eyes['left_eye']['x, y'][1], eyes_width, eyes_width))
        pygame.draw.rect(screen, eyes_colors,(self.segments[0][0] + eyes['right_eye']['x, y'][0], self.segments[0][1] + eyes['right_eye']['x, y'][1], eyes_width, eyes_width))
        pygame.draw.rect(screen, background_color,(self.segments[0][0] + eyes['left_eye']['pupil_y_x'][0], self.segments[0][1] + eyes['left_eye']['pupil_y_x'][1], pupil_width, pupil_width))
        pygame.draw.rect(screen, background_color,(self.segments[0][0] + eyes['right_eye']['pupil_y_x'][0], self.segments[0][1] + eyes['right_eye']['pupil_y_x'][1], pupil_width, pupil_width))

    def get_eyes_offset(self, dx, dy):
        self.eyes = {
            'left_eye': {
            'x, y': (10, 30),
            'pupil_y_x': (15, 35) 
            },
            'right_eye': {
            'x, y': (30, 30),
            'pupil_y_x': (35, 35) 
            }
        }
        if dx == -1:
            self.eyes = {
                'left_eye': {
                    'x, y': (10, 10),
                    'pupil_y_x': (15, 10) 
                },
                'right_eye': {
                    'x, y': (30, 10),
                    'pupil_y_x': (35, 10) 
                }
            }
        if dx == 1:
            self.eyes = {
                'left_eye': {
                    'x, y': (10, 30),
                    'pupil_y_x': (15, 35) 
                },
                'right_eye': {
                    'x, y': (30, 30),
                    'pupil_y_x': (35, 35) 
                }
            }
        if dy == -1:
            self.eyes = {
                'left_eye': {
                    'x, y': (10, 10),
                    'pupil_y_x': (15, 15) 
                },
                'right_eye': {
                    'x, y': (10, 30),
                    'pupil_y_x': (15, 35) 
                }
            }
        if dy == 1:
            self.eyes = {
                'left_eye': {
                    'x, y': (30, 10),
                    'pupil_y_x': (35, 15) 
                },
                'right_eye': {
                    'x, y': (30, 30),
                    'pupil_y_x': (35, 35) 
                }
            }
        return self.eyes



