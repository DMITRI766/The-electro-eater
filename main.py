import pygame
import random
from sys import exit


pygame.init()


WIDTH, HEIGHT = 800, 800
FPS = 15
SNAKE_BLOCK = 20
WALL_SIZE = 40


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')


back = pygame.image.load("floor.png").convert()
snake_head_down = pygame.image.load("head down.png").convert_alpha()
snake_head_up = pygame.image.load("head top.png").convert_alpha()
snake_head_left = pygame.image.load("lion's head.png").convert_alpha()
snake_head_right = pygame.image.load("The head is right.png").convert_alpha()
snake_tail = pygame.image.load("tail.png").convert_alpha()
food_image = pygame.image.load("meal.png").convert_alpha()
wall_image = pygame.image.load("wall.png").convert_alpha()


font_style = pygame.font.SysFont("bahnschrift", 25)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def load_walls(filename):
    walls = []
    with open(filename, 'r') as file:
        for y, line in enumerate(file.readlines()):
            for x, char in enumerate(line.strip()):
                if char == '1':
                    walls.append((x * WALL_SIZE, y * WALL_SIZE))
    return walls
def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1


    head_image = snake_head_down

    foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
    foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK

    walls = load_walls('lvl.txt')

    while not game_over:
        while game_close:
            screen.fill((0, 0, 0))
            message("You lost! Press C-Play Again or Q-Quit", (255, 0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:  # Влево
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                    head_image = snake_head_left
                elif event.key == pygame.K_d:  # Вправо
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                    head_image = snake_head_right
                elif event.key == pygame.K_w:  # Вверх
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                    head_image = snake_head_up
                elif event.key == pygame.K_s:  # Вниз
                    y1_change = SNAKE_BLOCK
                    x1_change = 0
                    head_image = snake_head_down


        if x1 >= WIDTH:
            x1 = 0  #
        elif x1 < 0:
            x1 = WIDTH - SNAKE_BLOCK
        if y1 >= HEIGHT:
            y1 = 0
        elif y1 < 0:
            y1 = HEIGHT - SNAKE_BLOCK

        x1 += x1_change
        y1 += y1_change
        screen.blit(back, (0, 0))


        for wall in walls:
            screen.blit(wall_image, wall)


        screen.blit(food_image, (foodx, foody))


        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]


        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True


        for wall in walls:
            if snake_head[0] == wall[0] and snake_head[1] == wall[1]:
                game_close = True


        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            length_of_snake += 1

        for index, segment in enumerate(snake_list):
            if index == len(snake_list) - 1:
                screen.blit(head_image, (segment[0], segment[1]))
            else:
                screen.blit(snake_tail, (segment[0], segment[1]))

        pygame.display.update()
        pygame.time.Clock().tick(FPS)

    pygame.quit()
    exit()

game_loop()
