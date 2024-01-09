import pygame
        
def get_tail_styles(snake):
    tail = snake[len(snake)-1]
    body = snake[len(snake)-2]
    dx = tail[0] - body[0]
    dy = tail[1] - body[1]
    if dx < 0:
        tail_styles = {
            'x_y': (25, 0),
            'width_tail_x_y': (25, 50)
        }
    if dx > 0:
        tail_styles = {
            'x_y': (0, 0),
            'width_tail_x_y': (25, 50)
        }
    if dy < 0:
        tail_styles = {
            'x_y': (0, 25),
            'width_tail_x_y': (50, 25)
        }
    if dy > 0:
        tail_styles = {
            'x_y': (0, 0),
            'width_tail_x_y': (50, 25)
        }
    return tail_styles 

def get_head_offset(dx, dy, snake):
    head = snake[0]
    body = snake[1]
    odx = head[0] - body[0]
    ody = head[1] - body[1]
    if ody < 0:
        ody = -1
    if ody > 0:
        ody = 1
    if odx < 0:
        odx = -1
    if odx > 0:
        odx = 1
    if dx == odx and dy == ody and dy == -1:
        head = {
            'x_y': (0, 25),
            'width_head_x_y': (50, 25)
        }
    if dx == odx and dy == ody and dy == 1:
        head ={
            'x_y': (0, 0),
            'width_head_x_y': (50, 25)
        }
    if dx == odx and dy == ody and dx == -1:
        head = {
            'x_y': (25, 0),
            'width_head_x_y': (25, 50)
        }
    if dx == odx and dy == ody and dx == 1:
        head = {
            'x_y': (0, 0),
            'width_head_x_y': (25, 50)
        }
    if dx != odx and dy != ody and (odx > 0 and dy < 0) or (odx > 0 and dy > 0):
        head = {
            'x_y': (0, 0),
            'width_head_x_y': (25, 50)
        }
    if dx != odx and dy != ody and (odx < 0 and dy > 0) or (odx < 0 and dy < 0):
        head = {
            'x_y': (25, 0),
            'width_head_x_y': (25, 50)
        }
    if dx != odx and dy != ody and (ody > 0 and dx < 0) or (ody > 0 and dx > 0):
        head = {
            'x_y': (0, 0),
            'width_head_x_y': (50, 25)
        }
    if dx != odx and dy != ody and (ody < 0 and dx > 0) or (ody < 0 and dx < 0):
        head = {
            'x_y': (0, 25),
            'width_head_x_y': (50, 25)
        }
    return head

def draw_eyes(eyes, screen, eyes_colors, background_color, snake, eyes_width, pupil_width):
    pygame.draw.rect(screen, eyes_colors,(snake[0][0] + eyes['left_eye']['x, y'][0], snake[0][1] + eyes['left_eye']['x, y'][1], eyes_width, eyes_width))
    pygame.draw.rect(screen, eyes_colors,(snake[0][0] + eyes['right_eye']['x, y'][0], snake[0][1] + eyes['right_eye']['x, y'][1], eyes_width, eyes_width))
    pygame.draw.rect(screen, background_color,(snake[0][0] + eyes['left_eye']['pupil_y_x'][0], snake[0][1] + eyes['left_eye']['pupil_y_x'][1], pupil_width, pupil_width))
    pygame.draw.rect(screen, background_color,(snake[0][0] + eyes['right_eye']['pupil_y_x'][0], snake[0][1] + eyes['right_eye']['pupil_y_x'][1], pupil_width, pupil_width))

def get_eyes_offset(dx, dy):
    eyes = {
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
        eyes = {
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
        eyes = {
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
        eyes = {
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
        eyes = {
            'left_eye': {
                'x, y': (30, 10),
                'pupil_y_x': (35, 15) 
            },
            'right_eye': {
                'x, y': (30, 30),
                'pupil_y_x': (35, 35) 
            }
        }
    return eyes

eyes_width = 10
pupil_width = 5

