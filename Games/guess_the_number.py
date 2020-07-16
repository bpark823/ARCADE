import random, math, os
import pygame

# Display
pygame.init()
size = WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("Guess the Number!")

# Colors
WHITE = [255, 255, 255]
BLACK = 0, 0, 0
BLUE = 0,0,255

# game loop variables
screen = pygame.display.set_mode(size, 0, 32)
fps = 60
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font("images/PressStart2P-Regular.ttf", 20)
num_font = pygame.font.Font("images/PressStart2P-Regular.ttf", 10)

# variables for drawing game buttons
GAP = 15
RADIUS = 20
numbers = []
startingx = 100
startingy = 400
n = 0
for i in range(20):
    n += 1
    x = startingx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 10))
    y = startingy + ((i // 10) * (GAP + RADIUS * 2))
    numbers.append([x, y, str(n), True])

# images rendering
images = []
guessTooLow = pygame.image.load(os.path.join("images", "guess1.jpg"))
guessTooHigh = pygame.image.load(os.path.join("images", "guess2.jpg"))
guessWin = pygame.image.load(os.path.join("images", "guesswin.jpg"))
guessLose = pygame.image.load(os.path.join("images", "guesslose.png"))
title = pygame.image.load(os.path.join("images", "gtntitle.png"))
images.extend((guessTooHigh, guessTooLow, guessWin, guessLose, title))

def sadness(number, true):
    for guessTaken in range(6):
        if int(number) < true:
            display_message("Guess too low, try again", 1)
            guessTaken += 1
            break
        elif int(number) > true:
            display_message("Guess too high, try again", 0)
            guessTaken += 1
            break
        elif int(number) == true:
            display_message("You win!", 2)
            break
        if guessTaken == 5:
            display_message("You lost...", 3)
            break

def draw():
    screen.fill(BLUE)
    drawText('GUESS A NUMBER BETWEEN 1-20: ', font, BLACK, screen, 125, 300)
    screen.blit(images[4], (250, 50))
    # draw buttons
    for num in numbers:
        x, y, n, visible = num
        if visible:
            pygame.draw.circle(screen, BLACK, (x, y), RADIUS, 3)
            text = num_font.render(n, 1, BLACK)
            screen.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))
    pygame.display.update()

def display_message(message, n):
    pygame.time.delay(500)
    screen.fill(BLUE)
    text = font.render(message, 1, BLACK)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    screen.blit(images[n], (250, 0))
    pygame.display.update()
    pygame.time.delay(1500)


def drawText(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def game():
    correct = random.randint(1, 20)
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for num in numbers:
                    x, y, n, visible = num
                    if visible:
                        dis = math.sqrt((x - mx) ** 2 + (y - my) ** 2)
                        if dis < RADIUS:
                            num[3] = False
                            sadness(num[2], correct)
        draw()



