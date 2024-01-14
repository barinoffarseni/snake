from random import randrange

def get_new_apple_coordinates(snake, width, size):
    generate_again = True
    while generate_again:
        apple = randrange(0 ,width, size), randrange(0 ,width, size)
        generate_again = False
        for part in snake:
            if part == apple:
                generate_again = True
                break
    return apple